from django.conf.urls import patterns, url
#comment from lucero
urlpatterns = patterns('apps.homepage.views',
	#url('', include('django.contrib.auth.urls')),
    url(r'^$', 'index', name="homepage_index"),
    url(r'^login/$', 'login_user', name="homepage_login"),
    url(r'^art/browse', 'abrowse', name="art_browse"),
    url(r'^writing/browse', 'wbrowse', name="writing_browse"),
 )

urlpatterns += patterns('',
	(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'homepage/login.html'}),
)