# from django.conf.urls import patterns, include, url

# # Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'djangoblog.views.home', name='home'),
#     # url(r'^djangoblog/', include('djangoblog.foo.urls')),

#     # Uncomment the admin/doc line below to enable admin documentation:
#     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#     # Uncomment the next line to enable the admin:
#     url(r'^admin/', include(admin.site.urls)),
# )



from posts.views import PostList, SearchResults
from django.conf.urls.defaults import patterns, include, url
from django.views.generic.base import RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
 
# urlpatterns = patterns('',
#   # Examples:
#   # url(r'^$', 'djangoblog.views.home', name='home'),
#   # url(r'^djangoblog/', include('djangoblog.foo.urls')),
 
#   # Uncomment the admin/doc line below to enable admin documentation:
#   # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
 
#   # Uncomment the next line to enable the admin:
#   url(r'^admin/', include(admin.site.urls), name='adminpage'),
 
#   url(r'^$', PostList.as_view(), name=u'mainpage'),
#   url(r'^posts/', PostList.as_view(), name=u'postlist'),
# )


urlpatterns = patterns('',
  # Examples:
  # url(r'^$', 'djangoblog.views.home', name='home'),
  # url(r'^djangoblog/', include('djangoblog.foo.urls')),
 
  # Uncomment the admin/doc line below to enable admin documentation:
  url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
 
  # Uncomment the next line to enable the admin:
  url(r'^admin/', include(admin.site.urls)),
 
  url(r'^$', RedirectView.as_view(url='/posts/')),
  url(r'^posts/', include('posts.urls')),
  url(r'^search/', SearchResults.as_view(), name="search"),
)