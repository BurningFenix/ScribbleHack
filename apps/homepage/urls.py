from django.conf.urls import *

urlpatterns = patterns('apps.homepage.views',
    url(r'^$', 'index', name="homepage_index"),
    url(r'^login/$', 'login', name="homepage_login"),
    #url(r'^browse/$', 'browse', name="homepage_browse"),
    #url(r'^confirmed/$', 'congrats', name="homepage_congrats"),
 )