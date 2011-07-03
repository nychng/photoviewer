from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
import settings
import os

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'photoviewer.homepage.views.home', name='home'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
					(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
				   )
