from datetime import datetime

from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect

from intellMEET import settings
from intellMEET.models import Roleuser, Role, Interviewer, Jobposition, Interview
from intellMEET.utils import not_found_404


def user_details(request: object):
    user = Roleuser.objects.filter(first_name=request.user).first()
    if user is not None:
        return render(request, 'user/user_profile.html', {"user": user})
    else:
        return not_found_404(request)


def save_profile(request: object):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name').split(' ')
        user = Roleuser.objects.filter(first_name=request.user).first()
        user.first_name, user.last_name, user.email, user.description = name[0], name[1], data.get('email'), data.get(
            'description')
        user.save()
        return user_details(request)
    else:
        return user_details(request)


def upload_profile_pic(request: object):
    if request.method == 'POST':
        data = request.FILES
        user = Roleuser.objects.filter(first_name=request.user).first()
        user.profilepicture = data.get('profile_pic')
        user.save()
        return user_details(request)
    else:
        return user_details(request)


def schedule_interview(request: object):
    user = User.objects.filter(username=request.user).first()
    if request.GET.get('date') is None:
        # give the result of current day
        i_date = datetime.today()
        # interviews = Interview.objects.filter(interviewdate=i_date)
        interviews = Interview.objects.filter(interviewdate=i_date)
        # TO DO
        # Get a list of user which can be used for transferring the interview slot.
        interviewers = Interviewer.objects.filter()
        # Jobposition.objects.filter()
        return render(request, 'user/schedule-interview.html', {'interviewers': interviewers,
                                                                'interviews': interviews})
    else:
        interviews = Interview.objects.filter(interviewdate=request.GET.get('date'))
        # Get a list of user which can be used for transferring the interview slot.
        interviewers = Interviewer.objects.all()
        # Jobposition.objects.filter()
        return render(request, 'user/slot-schedule.html', {'interviewers': interviewers,
                                                           'interviews': interviews})


def accept_slot(request: object):
    if settings.PRINT_LOG is True:
        print(request.POST)
    return redirect('schedule_interview')


def propose_schedule(request: object):
    return redirect('schedule_interview')


def transfer_schedule(request: object):
    return redirect('schedule_interview')
