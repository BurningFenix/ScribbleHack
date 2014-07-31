from django.conf.urls import patterns, url
from .views import Universe, WritingList

urlpatterns = patterns('',
	url(r'^$', Universe.as_view()),
	url(r'^writing/$', WritingList.as_view()),
)