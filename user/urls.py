from django.urls import re_path, include, path
from . import views

urlpatterns = [
    path('', views.user_details, name='user'),
    path('save_profile/', views.save_profile, name='save_profile'),
    path('upload_profile_pic/', views.upload_profile_pic, name='upload_profile_pic'),
    path('schedule_interview', views.schedule_interview, name='schedule_interview'),
    path('accept_slot/', views.accept_slot, name='accept_slot'),
    path('propose_schedule', views.propose_schedule, name='propose_schedule'),
    path('transfer_schedule', views.transfer_schedule, name='transfer_schedule'),
]
