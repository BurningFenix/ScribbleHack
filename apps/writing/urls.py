from django.conf.urls import patterns, url
from .views import WritingListView, CreateWritingView

urlpatterns = patterns('',
	url(r'^$', WritingListView.as_view()),
	url(r'^create', CreateWritingView.as_view(),
		name='create_writing'),
)