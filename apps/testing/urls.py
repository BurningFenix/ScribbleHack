from django.conf.urls import patterns, url
from .views import BrowseWritingView, HomepageView, EditProfileView, \
	ProfileView, ProfileEditJournalView, SubmitView, DisplayWritingView

urlpatterns = patterns('',
    url(r'^browse_writing/$', BrowseWritingView.as_view(),
    	name='browse_writing'),
    url(r'^homepage/$', HomepageView.as_view(),
    	name='homepage'),
    url(r'^edit_profile/$', EditProfileView.as_view(),
    	name='edit_profile'),
    url(r'^profile/$', ProfileView.as_view(),
    	name='profile'),
    url(r'^profile_edit_journal/$', ProfileEditJournalView.as_view(),
    	name='profile_edit_journal'),
    url(r'^submit/$', SubmitView.as_view(),
    	name='submit'),
    url(r'^display_writing/$', DisplayWritingView.as_view(),
    	name='display_writing'),
)
