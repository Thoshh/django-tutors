# -*- coding: utf-8 -*-

__revision__ = '$Id$'

from django.conf.urls.defaults import *

urlpatterns = patterns('uploads.views',
    (r'^static/$', 'static'),
    (r'^dynamic/$', 'dynamic'),
    (r'^handler/$', 'handler'),
)
