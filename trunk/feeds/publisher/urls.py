# -*- coding: utf-8 -*-

__revision__ = '$Id$'

from django.conf.urls.defaults import *

from publisher.views import feed
from publisher.feeds import UserEntriesFeed

published_feeds = {
    'entries': UserEntriesFeed,
}

urlpatterns = patterns('',
    (r'feeds/(?P<url>.*)/$', feed, {'feed_dict': published_feeds}),
)
