from django.conf.urls import patterns, url

urlpatterns = patterns('apps.homepage.views',
	#url('', include('django.contrib.auth.urls')),
    url(r'^$', 'index', name="homepage_index"),
    #url(r'^login/$', 'login_user', name="homepage_login"),
    url(r'^art/browse', 'abrowse', name="art_browse"),
    url(r'^writing/browse', 'wbrowse', name="writing_browse"),
 )

urlpatterns += patterns('',
	# so this follows the following format:
	# (regular expression, Python callback function [, optional_dictionary [, optional_name]])
	(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'homepage/login.html'}, 'homepage_login'),
)