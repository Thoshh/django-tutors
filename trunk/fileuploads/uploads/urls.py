# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('uploads.views',
    (r'^$', 'index'),
)
