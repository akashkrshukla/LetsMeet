"""intellMEET URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import PasswordResetConfirmView
from django.urls import path, include
from django.conf.urls.static import static
from intellMEET import views
from django.urls import path, include
from intellMEET import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(success_url='/accounts/login/'), name='password_reset_confirm'),
    path('candidate/', include('candidate.urls'), name='candidate'),
    path('jobs/', include('jobs.urls'), name='jobs'),
    path('user/', include('user.urls'), name='user'),
    path('tasks/', include('tasks.urls'), name='tasks'),
    path('branding/', include('branding.urls'), name='branding'),
    path('applicant/', include('applicant.urls'), name='applicant'),
    path('ajax/get_news_feed/', views.get_news_feed, name='get_news_feed')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL)
