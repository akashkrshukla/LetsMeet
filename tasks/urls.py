from django.urls import re_path, include, path
from . import views

urlpatterns = [
    path('', views.task_list, name='tasks')
]
