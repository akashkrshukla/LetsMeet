from django.urls import path
from candidate import views

urlpatterns = [
    path('', views.candidate_list, name='candidate'),
    path('candidate_detail/', views.candidate_detail, name='candidate_detail'),
    path('save_description/', views.save_description, name='save_description'),
    path('save_experience/', views.add_update_experience, name='save_experience'),
    path('save_summary/', views.save_summary, name='save_summary'),
    path('profile_image/', views.update_profile_image, name='profile_image'),
    path('update_skill/', views.update_skill, name='update_skill'),
    path('add_candidate/', views.add_candidate, name='add_candidate'),
    path('upload_candidate/', views.upload_candidate, name='upload_candidate'),
    path('download/', views.download_files, name='download')
]
