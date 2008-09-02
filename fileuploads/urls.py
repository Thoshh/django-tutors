# -*- coding: utf-8 -*-

__revision__ = '$Id$'

from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    (r'^uploads/', include('uploads.urls')),
)

if settings.DEBUG:
    urlpatterns = urlpatterns + patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )