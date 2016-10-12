"""simple_web_scraper URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from simple_web_scraper import views

urlpatterns = [
    url(r'^/$', views.home),
    url(r'^$', views.home),

    url(r'^admin/', include(admin.site.urls)),

    # /articles
    url(r'^api/rest/v1/articles/?$', views.ArticleList.as_view()),
    url(r'^api/rest/v1/articles/(?P<id>[0-9]+)/?$', views.ArticleDetail.as_view()),

    # /authors
    url(r'^api/rest/v1/authors/?$', views.AuthorList.as_view()),
    url(r'^api/rest/v1/authors/(?P<id>[0-9]+)/?$', views.AuthorDetail.as_view()),

    # /outlets
    url(r'^api/rest/v1/outlets/?$', views.OutletList.as_view()),
    url(r'^api/rest/v1/outlets/(?P<id>[0-9]+)/?$', views.OutletDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
