from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('apps.homepage.urls')),
    (r'^accounts/', include('apps.accounts.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
