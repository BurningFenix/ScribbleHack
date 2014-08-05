from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

handler404 = 'sh.views.custom404'

urlpatterns = patterns('',
    (r'^', include('apps.homepage.urls')),
    (r'^accounts/', include('apps.accounts.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'universe/', include('apps.universe.urls')),
    url(r'writing/', include('apps.writing.urls')),
    #url(r'^404/', 'sh.views.custom404')  # this is for testing
)
