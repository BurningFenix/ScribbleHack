from django.conf.urls import patterns, url

urlpatterns = patterns('apps.accounts.views',
    url(r'^profile/$', 'profile_view', name="profile"),
    url(r'^profile/edit', 'edit_profile_view', name="edit"),
    url(r'^logout/', 'logout_view', name='logout'),
    url(r'^register/', 'register_view', name='register')
 )

urlpatterns += patterns('',
	# so this follows the following format:
	# (regular expression, Python callback function [, optional_dictionary [, optional_name]])
	(r'^login/$', 'django.contrib.auth.views.login',
		{'template_name': 'accounts/login.html'},'login'),
)
