from django.conf.urls import patterns, url
from .views import UniverseView

urlpatterns = patterns('',
	url(r'^$', UniverseView.as_view()),
)