from django.conf.urls import patterns, url
from .views import UniverseView, WritingListView, CreateWritingView

urlpatterns = patterns('',
	url(r'^$', UniverseView.as_view()),
	url(r'^writing/$', WritingListView.as_view()),
	url(r'^writing/create', CreateWritingView.as_view(),
		name='create_writing'),
)