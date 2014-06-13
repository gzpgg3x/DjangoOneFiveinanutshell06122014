# -*- encoding: utf-8 -*-
from posts.views import PostList, PostDetails
from django.conf.urls import patterns, include, url
 
urlpatterns = patterns('',
  url(r'^$', PostList.as_view(), name='postlist'),
  url(r'^(?P<slug>[a-zA-Z0-9_-]+)/$',
      PostDetails.as_view(), name='postdetails'),
)