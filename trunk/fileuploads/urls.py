# -*- coding: utf-8 -*-

__revision__ = '$Id$'

from django.conf.urls.defaults import *

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    (r'^', include('uploads.urls')),
)
