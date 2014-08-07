from django.conf.urls import patterns, include, url
from .views import IndexView, ArtBrowseView
from django.contrib import admin
admin.autodiscover()

handler404 = 'sh.views.custom404'

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view()),
    url(r'^art$', ArtBrowseView.as_view()),
    url(r'^accounts/', include('apps.accounts.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'universe/', include('apps.universe.urls')),
    url(r'writing/', include('apps.writing.urls')),
    #url(r'^404/', 'sh.views.custom404')  # this is for testing
)
