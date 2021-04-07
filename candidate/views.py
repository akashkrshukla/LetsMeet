# write your views schema here.
import os

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.datetime_safe import datetime

from intellMEET.constants import CANDIDATE_IMAGE_PLACE_HOLDER
from intellMEET.models import Candidateexperience, Candidate, City, Candidateskill, Candidatesource
from intellMEET.utils import get_salary, not_found_404, get_all_countries, split_total_experience, handle_uploaded_file, \
    split_salary_amount, get_total_experience, read_excel, download, get_job_type


def candidate_list(request: object):
    cnd_list = Candidate.objects.all()
    return render(request, "create_candidate/create_candidate.html", {"cnd_list": cnd_list})


def get_all_cities():
    return City.objects.all()


def get_city(country: str):
    return City.objects.filter(fkcountry=country)


def candidate_detail(request: object):
    cnd_id = request.GET.get('cnd_id')
    if cnd_id:
        cnd_detail = Candidate.objects.get(id=cnd_id)
        if cnd_detail:
            cnd_detail.skills = Candidateskill.objects.filter(fkcandidate=cnd_detail)
            cnd_experience = Candidateexperience.objects.filter(fkcandidate=cnd_detail).order_by('-start_date')
            for item in cnd_experience:
                item.salary_lakhs, item.salary_thousands = split_salary_amount(item.salary)
            cnd_detail.cnd_experience = cnd_experience
            cnd_detail.total_experience_yr, cnd_detail.total_experience_month = split_total_experience(
                cnd_detail.total_experience)
            cnd_detail.ex_salary_lakhs, cnd_detail.ex_salary_thousands = split_salary_amount(cnd_detail.expected_salary)
            cnd_detail.cur_salary_lakhs, cnd_detail.cur_salary_thousands = split_salary_amount(
                cnd_detail.current_salary)
            # print(item._meta.get_fields())
            return render(request, "create_candidate/candidate_details.html", {'cnd_detail': cnd_detail,
                                                                               'cntry_list': get_all_countries(),
                                                                               'city_list': get_all_cities()})
        else:
            return candidate_list(request)
    else:
        return candidate_list(request)


def save_description(request: object):
    values = request.POST
    cnd = Candidate.objects.filter(id=request.GET['cnd_id']).first()
    city = City.objects.filter(cityname=values.get('city')).first()
    cnd.description, cnd.email, cnd.mobileno, cnd.street_name, cnd.fkcity, cnd.fkcountry = values.get(
        'description'), values.get(
        'email'), values.get('mobileno'), values.get('street'), city, city.fkcountry
    cnd.save()
    return candidate_detail(request)


def add_update_experience(request: object):
    values = request.POST
    exp_id = request.GET.get('exp_id')
    current_employer = '1' if values.get('current_employer') == 'on' else '0'
    exp = Candidateexperience.objects.filter(id=exp_id).first()
    if exp:
        edit_experience(request, current_employer, exp_id)
    else:
        add_experience(request, current_employer)
    return candidate_detail(request)


def add_experience(request: object, current_emp: str):
    values = request.POST
    cnd = Candidate.objects.filter(id=request.GET.get('cnd_id')).first()
    cnd_experience = Candidateexperience(company=values.get('company'), position=values.get('position'),
                                         current_employer=current_emp,
                                         job_type=values.get('job_type'),
                                         salary=get_salary(values.get('salary_lakhs'), values.get('salary_thousands')),
                                         start_date=values.get('tenure_from'),
                                         end_date=values.get('tenure_to'),
                                         fkcandidate=cnd)
    cnd_experience.save()


def edit_experience(request: object, current_emp: str, exp_id: str):
    values = request.POST
    exp = Candidateexperience.objects.filter(id=exp_id).first()
    exp.company, exp.position, exp.current_employer, exp.job_type, exp.salary, exp.start_date, exp.end_date = values.get(
        'company'), values.get('position'), current_emp, values.get('job_type'), get_salary(values.get('salary_lakhs'),
                                                                                            values.get(
                                                                                                'salary_thousands')), values.get(
        'tenure_from') if values.get(
        'tenure_from') else datetime.now().today(), values.get('tenure_to') if values.get(
        'tenure_to') else datetime.now()
    exp.save()


def save_summary(request: object):
    cnd_id = request.GET.get('cnd_id')
    if request.method == 'POST' and cnd_id:
        data = request.POST
        Candidate.objects.filter(id=cnd_id).update(
            total_experience=get_total_experience(data.get('tot_exp_years'), data.get('tot_exp_months')),
            expected_salary=get_salary(data.get('ex_lakhs'), data.get('ex_thousands')), dob=data.get('dob'),
            notice_period_days=data.get('notice_period_days'), gender=data.get('gender'), name=data.get('name'),
        )
        return candidate_detail(request)
    else:
        return not_found_404(request)


def update_profile_image(request: object):
    cnd = Candidate.objects.filter(id=request.GET.get('cnd_id')).first()
    if cnd:
        filename = handle_uploaded_file(request.FILES.get('profile_image'), os.path.join('static', 'media',
                                                                                         'profile_images'),
                                        os.path.join('media', 'profile_images'))
        cnd.candidate_image = filename
        cnd.save()
        return candidate_detail(request)
    else:
        return candidate_detail(request)


# get skl_id & skill as input and update if skl_id exist
# add new skills if no skl_id is present
# just skl_id : delete skill
# just skill: add skill
# skl_id & skill: update skill
def update_skill(request: object):
    data = request.POST
    skl_id = data.get('skl_id')
    skill = data.get('skill')
    if skl_id is None and len(skill.strip()) > 1:
        # Do add this skill
        user = Candidate.objects.filter(id=request.GET.get('cnd_id')).first()
        cnd_skill = Candidateskill(skill=skill, fkcandidate=user)
        cnd_skill.save()
    else:
        Candidateskill.objects.filter(id=skl_id).delete()
    return candidate_detail(request)


def add_candidate(request: object):
    data = request.POST
    filename = handle_uploaded_file(request.FILES.get('resume'), os.path.join('static', 'media', 'resumes'),
                                    os.path.join('media', 'resumes'))
    cnd = Candidate(name=data.get('name'), email=data.get('email'), gender=data.get('gender'),
                    current_salary=data.get('cur_salary')
                    , notice_period_days=data.get('notice_period'),
                    candidate_image=CANDIDATE_IMAGE_PLACE_HOLDER, resume=filename,
                    createddate=datetime.now().today(), lastmodifed=datetime.now().today(), created_by=request.user)
    cnd.save()

    skills = str(data.get('skills')).split(",")

    for skill in skills:
        cnd_skill = Candidateskill(skill=skill, fkcandidate=cnd)
        cnd_skill.save()

    return redirect('candidate')


def upload_candidate(request: object):
    file = request.FILES.get('candidate_sheet')
    if file is None:
        return candidate_list(request)
    failed_count = 0
    cnd_data = read_excel(file)
    for item in cnd_data:
        # save source
        source = Candidatesource.objects.filter(name=item[20]).first()
        if source is None:
            source = Candidatesource()
            source.name = item[20]
            source.save()
        # save candidate
        cnd = Candidate(name=item[0], email=item[1], mobileno=item[2], current_company=item[5],
                        current_position=item[6],
                        total_experience=item[8] * 12, dob=datetime.strptime(item[10], "%d/%m/%Y").strftime("%Y-%m-%d"),
                        current_salary=item[12], expected_salary=item[13], job_type=get_job_type(item[14]),
                        notice_period_days=item[16], gender=item[19], fkcandidatesource=source,
                        lastmodifed=datetime.now().today(), candidate_image=CANDIDATE_IMAGE_PLACE_HOLDER,
                        createddate=datetime.now().today(), created_by=str(request.user))
        cnd.save()

        cnd.fkcandidatesource = source
        cnd.save()

        # save candidate skills
        # multiple values in excel under skills are to be comma separated
        skills = item[11].split(",")
        for skill in skills:
            skill_set = Candidateskill()
            skill_set.skill, skill_set.fkcandidate = skill, cnd
            skill_set.save()

    # return the list of candidates.
    return redirect('candidate')


def download_files(request: object):
    filename = request.GET.get('file')
    filepath = 'resources/' + filename
    if filename is None:
        return HttpResponse({})
    return download(request, filepath)
