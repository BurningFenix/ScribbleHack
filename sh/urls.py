from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sh.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^', include('apps.homepage.urls')),
    (r'^', include('apps.accounts.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
