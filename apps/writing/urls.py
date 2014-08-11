from django.conf.urls import patterns, url
from .views import WritingListView, CreateWritingView, WritingDetailView, \
	EditWritingView

urlpatterns = patterns('',
	url(r'^$', WritingListView.as_view(), name='index'),
	url(r'^create/$', CreateWritingView.as_view(),
		name='create'),
	url(r'^(?P<pk>\d+)/$', WritingDetailView.as_view(),
		name='detail'),
	url(r'^(?P<pk>\d+)/edit/$', EditWritingView.as_view(),
		name='edit'),
)