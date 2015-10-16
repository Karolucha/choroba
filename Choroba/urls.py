"""Choroba URL Configuration

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
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'portal.views.index', name='home'),
    url(r'^search_disease/', 'portal.views.search_disease'),
    url(r'^articles/', 'portal.views.articles'),
    url(r'^disease/(?P<disease_id>\w+)', 'portal.views.disease'),
    url(r'^added_comment', 'portal.views.add_comment'),
    url(r'^article/(?P<article_id>\w+)', 'portal.views.article'),
    url(r'^account/$', 'portal.user_views.account'),
    url(r'^profile/(?P<user_id>\w+)/$', 'portal.user_views.profile'),
    url(r'^add_friend/$', 'portal.user_views.add_friend'),
    # url(r'^change_profile/$', 'portal.user_views.change_profile'),
    url(r'^login/$', 'portal.user_views.logging'),
    url(r'^logout/$', 'portal.user_views.logouting'),
]
