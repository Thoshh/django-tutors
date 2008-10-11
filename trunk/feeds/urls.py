# -*- coding: utf-8 -*-

__revision__ = '$Id$'

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^', include('publisher.urls')),
)
