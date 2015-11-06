"""scenario1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^taskmanager/', include('taskmanager.urls')),
    url(r'^admin/', include(admin.site.urls)),
    

    #url(r'^accounts', 'scenario1.views.account_main'),
    url(r'^accounts/login/$',  'scenario1.views.login'),
    url(r'^accounts/auth/$',  'scenario1.views.auth_view'),    
    url(r'^accounts/logout/$', 'scenario1.views.logout'),
    url(r'^accounts/loggedin/$', 'scenario1.views.loggedin'),
    url(r'^accounts/invalid/$', 'scenario1.views.invalid_login'),  
    url(r'^accounts/register/$', 'scenario1.views.register_user'),
    url(r'^accounts/register_success/$', 'scenario1.views.register_success'),  

]
