from django.conf.urls import *

urlpatterns = patterns('apps.homepage.views',
    url(r'^$', 'index', name="homepage_index"),
    url(r'^login/$', 'login', name="homepage_login"),
    url(r'^art/browse', 'abrowse', name="art_browse"),
    url(r'^writing/browse', 'wbrowse', name="writing_browse"),
 )