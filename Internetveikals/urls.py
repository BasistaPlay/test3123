"""Internetveikals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from majaslapa.views import *
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.i18n import i18n_patterns
from majaslapa import views
from django.conf.urls import url
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sakums, name='sakums'),
    path('account/', account, name='account'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', loginpage, name='login'),
    path('register/', register, name='register'),
    path('search/', search, name='search'),
    path('logout/', logoutUser, name='logout'),
    path('accounts/', include('allauth.urls')),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),



    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='majaslapa/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='majaslapa/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='majaslapa/password_reser_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='majaslapa/password_reser_done.html'), name='password_reset'),

    path('i18n/',include('django.conf.urls.i18n')),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),


] + i18n_patterns(
    path('', sakums, name='sakums'),
    path('account/', account, name='account'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', loginpage, name='login'),
    path('register/', register, name='register'),
    path('search/', search, name='search'),
    path('logout/', logoutUser, name='logout'),
    path('accounts/', include('allauth.urls')),

)

SOCIAL_AUTH_URL_NAMESPACE = 'social'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)