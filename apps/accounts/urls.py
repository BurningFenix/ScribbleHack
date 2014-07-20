from django.conf.urls import *

urlpatterns = patterns('apps.accounts.views',
    url(r'^profile/', 'profile', name="accounts_profile"),
    url(r'^profile/edit', 'edit_profile', name="accounts_edit"),
    #url(r'^browse/$', 'browse', name="homepage_browse"),
    #url(r'^confirmed/$', 'congrats', name="homepage_congrats"),
 )