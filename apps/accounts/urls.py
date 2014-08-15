from django.conf.urls import patterns, url
from .views import IndexView, LogoutView, ProfileView,\
	RegisterView, EditProfileView

urlpatterns = patterns('apps.accounts.views',
	url(r'^$', IndexView.as_view(), name="index"),
    url(r'^profile/(?P<pk>\d+)?$', ProfileView.as_view(), name="profile"),
    url(r'^profile/edit/$', EditProfileView.as_view(), name="edit"),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
 )

urlpatterns += patterns('',
	# so this follows the following format:
	# (regular expression, Python callback function [, optional_dictionary [, optional_name]])
	(r'^login/$', 'django.contrib.auth.views.login',
		{'template_name': 'accounts/login.html'},'login'),
)
