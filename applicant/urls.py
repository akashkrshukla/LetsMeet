from django.urls import re_path, include, path
from . import views

urlpatterns = [
    path('', views.applicant_login, name='applicant'),
    path('applicant_detail', views.applicant_detail, name='applicant_detail'),
    path('record_interview_video', views.record_interview_video, name='record_interview_video'),
    # schedule interview is applicable only for two way interview.
    path('schedule_applicant_interview', views.schedule_interview, name='schedule_applicant_interview'),
    path('my_interviews', views.my_interviews, name='my_interviews'),
    path('ajax/fix_interview_slot/', views.fix_interview_slot, name='fix_interview_slot'),
    path('ajax/get_available_slots/', views.get_available_slots, name='get_available_slots')
]
