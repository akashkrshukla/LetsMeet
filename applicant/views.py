import os
from datetime import date, datetime, time, timedelta

from dateutil import parser
from django.shortcuts import render, redirect

from intellMEET import settings
from intellMEET.models import Interview, InterviewSlot
from intellMEET.utils import send_mail, not_found_404
from django.utils.timezone import make_aware


def applicant_login(request: object):
    return render(request, 'applicant/applicant_login.html', {})


def applicant_detail(request):
    return render(request, 'applicant/applicant_detail.html', {})


def record_interview_video(request: object):
    return render(request, 'applicant/interview_video_oneway.html', {})


def schedule_interview(request: object):
    int_id = request.GET.get('int_id')
    interview = Interview.objects.filter(id=int_id).first()
    if interview is None:
        return not_found_404(request)
    if settings.PRINT_LOG is True:
        print(interview, int_id)
    total_slots_a_day = InterviewSlot.objects.filter(slottype=interview.fkjobapplication.fkjobposition.slottype)
    posted_date = interview.fkjobapplication.fkjobposition.posteddate
    close_date = interview.fkjobapplication.fkjobposition.closedate
    int_dates = []  # interview dates
    # return data for first date i.e. for posteddate. Rest slot data will be fetched through the ajax call.

    for index, day in enumerate(range((close_date - posted_date).days)):
        int_dates.append((posted_date + timedelta(days=index)))
    # booked slots are the slots that have been booked in a day
    booked_slots = Interview.objects.filter(fkjobapplication__fkjobposition__positioncode=
                                            interview.fkjobapplication.fkjobposition.positioncode,
                                            interviewdate=posted_date
                                            )
    for slot in total_slots_a_day:
        for b_slot in booked_slots:
            # print(timedelta(days=index), b_slot.interviewdate)
            if b_slot.fkinterviewslot_id == slot.id:
                slot.booked = 1
    if interview is None:
        return redirect('applicant_detail')
    else:
        return render(request, 'applicant/schedule_interview.html', {
            'interview': interview, 'slots': total_slots_a_day,
            'posted_date': posted_date, 'int_dates': int_dates
        })


def my_interviews(request: object):
    # TO DO
    # Please map the candidate with the logged in candidate for filtering the interview records.
    interviews = Interview.objects.all()
    return render(request, 'applicant/my_interviews.html', {
        'interviews': interviews
    })


def fix_interview_slot(request: object):
    interview = Interview.objects.filter(id=request.GET.get('int_id'))
    chosen_date = make_aware(parser.parse(request.GET.get('chosen_date')))
    if interview is None:
        pass
        # interview not found
    else:
        interview.update(fkinterviewslot=request.GET.get('chosen_slot'),
                         interviewdate=chosen_date)
    return get_available_slots(request)


def get_available_slots(request: object):
    int_id = request.GET.get('int_id')
    interview = Interview.objects.filter(id=int_id).first()
    total_slots_a_day = InterviewSlot.objects.filter(slottype=interview.fkjobapplication.fkjobposition.slottype)
    chosen_date = make_aware(parser.parse(request.GET.get('chosen_date')))
    booked_slots = Interview.objects.filter(fkjobapplication__fkjobposition__positioncode=
                                            interview.fkjobapplication.fkjobposition.positioncode,
                                            interviewdate=chosen_date
                                            )
    for slot in total_slots_a_day:
        for b_slot in booked_slots:
            if b_slot.fkinterviewslot_id == slot.id:
                slot.booked = 1
                 
    return render(request, 'applicant/interview_slots.html', {'slots': total_slots_a_day})
