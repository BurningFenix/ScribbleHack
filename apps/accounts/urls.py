from django.conf.urls import *

urlpatterns = patterns('apps.accounts.views',
    url(r'^profile/$', 'profile', name="accounts_profile"),
    url(r'^profile/edit', 'edit_profile', name="accounts_edit"),
 )