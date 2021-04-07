from django.urls import re_path, include, path
from . import views

urlpatterns = [
    path('', views.jobs_list, name='jobs'),
    path('create_job/', views.create_job, name='create_job'),
    path('save_job/', views.save_job, name='save_job'),
    path('create_interview/', views.create_interview, name='create_interview'),
    path('save_interview/', views.save_interview, name='save_interview'),
    path('candidate_invitation/', views.candidate_invitation, name='candidate_invitation'),
    path('applicant_list/', views.applicant_list, name="applicant_list"),
    path('close_job/', views.close_job, name='close_job'),
    path('archive_job/', views.archive_job, name='archive_job'),
    path('ajax/get_interviewers/', views.get_interviewers, name='get_interviewers'),
    path('edit_job/', views.edit_job, name='edit_job')
]
