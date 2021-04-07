import os
from datetime import datetime, timedelta

from django.db.models import Q, Sum
from django.shortcuts import render, redirect

from intellMEET.constants import UNRESPONSIVE_JOBS_DURATION_DAYS, job_position, RECRUITER_ROLE
from intellMEET.models import Customer, Jobposition, Department, Country, City, Academicqualification, Jobapplication, \
    Candidate, Roleuser, Interviewer, Interviewpanel
from intellMEET.utils import get_all_countries, get_all_cities, handle_uploaded_file, \
    get_job_type, get_academic_qualifications, get_all_department, get_all_customers, get_job_stage, get_form_errors, \
    get_relative_change
from jobs.dto import JobPositionDto


def jobs_list(request):
    archived = 0
    last_month = datetime.today() - timedelta(days=30)
    rel_change_pending_jobs = 0
    rel_change_total_jobs = 0
    if request.GET.get('archived') is None:
        # filter jobs other than archived jobs
        recent_candidate = Candidate.objects.all().order_by("-id").values('id', 'name', 'current_position',
                                                                          'candidate_image')[:10]
        applicant_count = Jobapplication.objects.all().count()

        # calculate job type data
        job_list = Jobposition.objects.filter(~Q(status=job_position.get('ARCHIVED_CODE'))).order_by("-posteddate")
        total_jobs = len(job_list)
        pending_jobs = len(Jobposition.objects.filter(~Q(status=job_position.get('ARCHIVED_CODE')),
                                                      jobapplication__isnull=True))
        ending_soon = len(Jobposition.objects.filter(
            ~Q(status=job_position.get('ARCHIVED_CODE')),
            closedate__range=[datetime.now(), (datetime.now() + timedelta(days=UNRESPONSIVE_JOBS_DURATION_DAYS))]))
        unresponsive_jobs = len(Jobposition.objects.filter(
            ~Q(status=job_position.get('ARCHIVED_CODE')), jobapplication__isnull=True))

        # calculate analytics data
        rel_change_pending_jobs = get_relative_change(pending_jobs, Jobposition.objects.filter(
            ~Q(status=job_position.get("ARCHIVED_CODE")), jobapplication__isnull=True,
            posteddate__lte=last_month).count())
        rel_change_total_jobs = get_relative_change(total_jobs, Jobposition.objects.filter(
            ~Q(status=job_position.get('ARCHIVED_CODE')), posteddate__lte=last_month).count())
        rel_change_ending_soon = get_relative_change(ending_soon, Jobposition.objects.filter(
            ~Q(status=job_position.get("ARCHIVED_CODE")),
            closedate__range=[last_month, (last_month + timedelta(days=UNRESPONSIVE_JOBS_DURATION_DAYS))]).count())
        rel_change_unresponsive = get_relative_change(unresponsive_jobs, Jobposition.objects.filter(
            ~Q(status=job_position.get('ARCHIVED_CODE')), jobapplication__isnull=True,
            posteddate__lte=last_month).count())
        tot_openings = Jobposition.objects.aggregate(Sum('openings'))

        # get department data.
        departments = get_all_department()
        for item in departments:
            item.total_jobs, item.completed_jobs = Jobposition.objects.filter(
                ~Q(status=job_position.get('ARCHIVED_CODE')), fkdepartment=item).count(), Jobposition.objects.filter(
                ~Q(status=job_position.get('ARCHIVED_CODE')), status=job_position.get('CLOSED_CODE'),
                fkdepartment=item).count()

    else:
        # archived filter should be applied to overall dashboard analytics data.
        # reference MEET 43 : Jira
        archived = 1
        recent_candidate = Candidate.objects.all().order_by("-id").values('id', 'name', 'current_position',
                                                                          'candidate_image')[:10]
        applicant_count = Jobapplication.objects.all().count()

        # get job data
        job_list = Jobposition.objects.filter(Q(status=job_position.get('ARCHIVED_CODE'))).order_by("-posteddate")
        total_jobs = len(job_list)
        pending_jobs = len(Jobposition.objects.filter(Q(status=job_position.get('ARCHIVED_CODE')),
                                                      jobapplication__isnull=True))
        ending_soon = len(Jobposition.objects.filter(
            Q(status=job_position.get('ARCHIVED_CODE')),
            closedate__range=[datetime.now(), (datetime.now() + timedelta(days=UNRESPONSIVE_JOBS_DURATION_DAYS))]))
        unresponsive_jobs = len((
            Jobposition.objects.filter(Q(status=job_position.get('ARCHIVED_CODE')), jobapplication__isnull=True)))

        # calculate analytics data
        rel_change_pending_jobs = get_relative_change(pending_jobs, Jobposition.objects.filter(
            Q(status=job_position.get("ARCHIVED_CODE")), jobapplication__isnull=True,
            posteddate__lte=last_month).count())
        rel_change_total_jobs = get_relative_change(total_jobs, Jobposition.objects.filter(
            Q(status=job_position.get('ARCHIVED_CODE')), posteddate__lte=last_month).count())
        rel_change_ending_soon = get_relative_change(ending_soon, Jobposition.objects.filter(
            Q(status=job_position.get("ARCHIVED_CODE")),
            closedate__range=[last_month, (last_month + timedelta(days=UNRESPONSIVE_JOBS_DURATION_DAYS))]).count())
        rel_change_unresponsive = get_relative_change(unresponsive_jobs, Jobposition.objects.filter(
            Q(status=job_position.get('ARCHIVED_CODE')), jobapplication__isnull=True,
            posteddate__lte=last_month).count())
        tot_openings = Jobposition.objects.aggregate(Sum('openings'))

        # get department data
        departments = get_all_department()
        for item in departments:
            item.total_jobs, item.completed_jobs = Jobposition.objects.filter(fkdepartment=item).count(), \
                                                   Jobposition.objects.filter(status=job_position.get('CLOSED_CODE'),
                                                                              fkdepartment=item).count()
    return render(request, "jobs/jobs.html", {"jobs_list": job_list,
                                              "total_jobs": total_jobs, "pending_jobs": pending_jobs,
                                              "unresponsive_jobs": unresponsive_jobs, "ending_soon": ending_soon,
                                              'departments': departments,
                                              "applicant_count": applicant_count,
                                              "recent_candidate": recent_candidate,
                                              "archived": archived,
                                              'rel_change_total_jobs': rel_change_total_jobs,
                                              'rel_change_pending_jobs': rel_change_pending_jobs,
                                              'rel_change_ending_soon': rel_change_ending_soon,
                                              'rel_change_unresponsive': rel_change_unresponsive,
                                              'tot_openings': tot_openings})


# Method is called for creating new job.
# send back fields/data to be auto-populated in HTML form.
# any auto-increment fields have to populated here.
def create_job(request: object):
    # this is new job being created.
    form_errors = get_form_errors(request)
    recruiters = Roleuser.objects.filter(fkrole__type=RECRUITER_ROLE)
    if form_errors is None:
        return render(request, "jobs/create_jobs.html", {'cntry_list': get_all_countries(),
                                                         'city_list': get_all_cities(),
                                                         'academic': get_academic_qualifications(),
                                                         'departments': get_all_department(),
                                                         'clients': get_all_customers(),
                                                         'recruiters': recruiters})
    else:
        return render(request, "jobs/create_jobs.html", {'cntry_list': get_all_countries(),
                                                         'city_list': get_all_cities(),
                                                         'academic': get_academic_qualifications(),
                                                         'departments': get_all_department(),
                                                         'clients': get_all_customers(),
                                                         'recruiters': recruiters,
                                                         'form_errors': request.form_errors})


def save_job(request: object):
    # create job & if successful redirect to create_job with blank form & success message
    # if fails creation of job return filled form with error messages.
    if request.method == 'POST':
        job_positions = JobPositionDto(request.POST)
        if job_positions.is_valid():
            data = request.POST
            customer = get_or_create_customer(data.get('client'))
            dept = get_or_create_department(data.get('department'))
            city = City.objects.filter(cityname=data.get('city')).first()
            country = Country.objects.filter(countryname=data.get('country')).first()
            academic_qualification = Academicqualification.objects.filter(name=data.get('min_education')).first()
            attach_file = handle_uploaded_file(request.FILES.get('attachfile'),
                                               os.path.join('static', 'media', 'job_attach_files'),
                                               os.path.join('media', 'job_attach_files'))
            recruiter = Roleuser.objects.filter(email=data.get('prim_recruiter')).first()
            jb_position = Jobposition(jobtitle=data.get('job_title'), fkcustomer=customer, fkdepartment=dept,
                                      posteddate=datetime.now().date(), closedate=data.get('closed_date'), lastmodifed=
                                      datetime.now().date(), fkcountry=country, fkcity=city,
                                      minexperience=data.get('tot_exp_min'), maxexperience=data.get('tot_exp_max'),
                                      keyskills=data.get('skills'), status=get_job_stage(data.get('stage')),
                                      attachfile=attach_file, jobdecription=data.get('description'),
                                      minpackage=data.get('min_ctc'), maxpackage=data.get('max_ctc'),
                                      jobtype=get_job_type(data.get('job_type')),
                                      fkacademicqualification=academic_qualification, positioncode=data.get('job_code'),
                                      certification=data.get('certifications'), otherinfo=data.get('other_info'),
                                      created_by=str(request.user), fkRoleUser=recruiter, openings=data.get('openings'),
                                      interviewers=data.get('interviewers'), slottype=data.get('slottype')
                                      )
            jb_position.save()
            # create and save interview panel
            # interview_panel = Interviewpanel(
            #     fkinterviewer=Interviewer.objects.filter(id=data.get('interviewers')).first(),
            #     fkJobPosition=jb_position)
            # interview_panel.save()

            return jobs_list(request)
        else:
            request.form_errors = job_positions.errors
            return create_job(request)


def create_interview(request: object):
    data = {}
    return render(request, "jobs/create_interview.html", {"interview_data": data})


def save_interview(request: object):
    data = {}
    # create job & if successful redirect to create_job with blank form & success message
    # if fails creation of job return filled form with error messages.
    return create_interview(request)


def candidate_invitation(request: object):
    data = {}
    return render(request, "jobs/candidate_invitation.html", {"invite_data": data})


def get_or_create_customer(user_id: int):
    customer = Customer.objects.filter(id=user_id).first()
    if customer is None:
        return None
    else:
        return customer


def get_or_create_department(dept_name):
    dept = Department.objects.filter(id=dept_name).first()
    if dept is None:
        return None
    else:
        return dept


def applicant_list(request):
    positioncode = request.GET.get('job_id')
    if positioncode is None:
        return jobs_list(request)
    else:
        job = Jobposition.objects.filter(positioncode=positioncode).first()
        job.applicant = Jobapplication.objects.filter(fkjobposition=job)
        return render(request, 'jobs/applicant_list.html', {"job": job})


# Job stages as per UI
# 0. Closed
# 1. Active
# 2. Lead
# 3. Suggested
# 4. Submitted
# 5. Final Interview
# 6. Offer Accepted.
# 7. Archived

def close_job(request):
    job_id = request.GET.get('job_id')
    Jobposition.objects.filter(positioncode=job_id).update(status=job_position.get('CLOSED_CODE'))
    return applicant_list(request)


def archive_job(request):
    job_id = request.GET.get('job_id')
    Jobposition.objects.filter(positioncode=job_id).update(status=job_position.get('ARCHIVED_CODE'))
    return redirect('jobs')


def get_interviewers(request: object):
    customer = Customer.objects.filter(id=request.GET.get('client')).first()
    interviewers = Interviewer.objects.filter(fkcustomer=customer)
    return render(request, 'jobs/interviewers_list.html', {'interviewers': interviewers})


def edit_job(request: object):
    # user is trying to edit the job.
    job = Jobposition.objects.filter(positioncode=request.GET.get('job_id')).first()
    recruiters = Roleuser.objects.filter(fkrole__type=RECRUITER_ROLE)
    if job is not None:
        departments = get_all_department()
        return render(request, 'jobs/edit_job.html', {'job': job,
                                                      'departments': departments,
                                                      'cntry_list': get_all_countries(),
                                                      'city_list': get_all_cities(),
                                                      'recruiters': recruiters
                                                      })
