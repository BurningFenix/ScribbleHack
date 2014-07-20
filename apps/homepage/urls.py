from django.conf.urls import *

urlpatterns = patterns('apps.homepage.views',
	#url('', include('django.contrib.auth.urls')),
    url(r'^$', 'index', name="homepage_index"),
    url(r'^login/$', 'login_user', name="homepage_login"),
    #url(r'^browse/$', 'browse', name="homepage_browse"),
    #url(r'^confirmed/$', 'congrats', name="homepage_congrats"),
 )

urlpatterns += patterns('',
	(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'homepage/login.html'}),
)