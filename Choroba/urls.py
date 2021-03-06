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
import portal.rest as rest

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'portal.views.index', name='home'),
    url(r'^search_disease/', 'portal.views.search_disease'),
    url(r'^disease/(?P<disease_id>\w+)/$', 'portal.views.disease'),
    url(r'^add_disease/$', 'portal.views.add_disease'),

    url(r'^discussion/(?P<discussion_id>\w+)/$', 'portal.views.discussion'),
    url(r'^add_discussion/$', 'portal.views.add_discussion'),
    url(r'^add_comment', 'portal.views.add_comment'),
    url(r'^add_specific_comment', 'portal.views.add_specific_comment'),
    url(r'^like_comment', 'portal.views.like_comment'),

    url(r'^hots/', 'portal.views.hots'),
    url(r'^question/(?P<question_id>\w+)/$', 'portal.views.question'),
    url(r'^api_question/(?P<question_id>\w+)/$', 'portal.views.api_question'),



    url(r'^articles/', 'portal.views.articles'),
    url(r'^article/(?P<article_id>\w+)/$', 'portal.views.article'),
    url(r'^add_article/', 'portal.views.add_article'),

    url(r'^account/$', 'portal.user_views.account'),
    url(r'^account_api/(?P<account_id>\w+)/$', 'portal.user_views.account_api'),
    url(r'^register/$', 'portal.user_views.register'),
    url(r'^profile/(?P<user_id>\w+)/$', 'portal.user_views.profile'),

    url(r'^search_friend/(?P<friend>\w+/)$', 'portal.user_views.search_friend'),
    url(r'^add_friend/(?P<user_id>\w+)/$', 'portal.user_views.add_friend'),
    url(r'^inviting/$', 'portal.user_views.inviting'),
    # url(r'^change_profile/$', 'portal.user_views.change_profile'),

    url(r'^login/$', 'portal.user_views.logging'),
    url(r'^logging_api/$', 'portal.user_views.logging_api'),
    url(r'^logout/$', 'portal.user_views.logouting'),

    url(r'^api/get_disease/', 'portal.views.get_disease', name='get_disease'),
    url(r'^api/get_article/', 'portal.views.get_article', name='get_article'),
    url(r'^api/get_friends/', 'portal.user_views.get_friends', name='get_friends'),

    #REST api
     url(r'^comments/$', rest.comments_list),
]
