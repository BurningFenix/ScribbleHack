from django.conf.urls import patterns, url
from .views import WritingListView, CreateWritingView, WritingDetailView

urlpatterns = patterns('',
	url(r'^$', WritingListView.as_view(), name='index'),
	url(r'^create/$', CreateWritingView.as_view(),
		name='create'),
	url(r'^(?P<pk>\d+)/$', WritingDetailView.as_view(),
		name='detail'),
)