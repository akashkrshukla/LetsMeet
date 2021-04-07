from django.urls import re_path, include, path
from . import views

urlpatterns = [
    path('', views.show_branding_customer, name='branding'),
    path('save_branding/', views.save_branding, name='save_branding'),
    path('show_branding/', views.get_branding_data, name='show_branding'),
    path('show_preview/', views.show_preview, name='show_preview'),
    path('add_section/', views.add_section, name='add_section'),
    path('save_template/', views.save_template, name='save_template'),
]
