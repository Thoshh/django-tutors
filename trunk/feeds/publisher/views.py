# -*- coding: utf-8 -*-

__revision__ = '$Id$'

from django.contrib.syndication.views import feed as orig_feed

def feed(request, url, feed_dict):
    user = 'joe'
    if url == 'entries':
        url = '%s/%s' % (url, user)
    return orig_feed(request, url, feed_dict)
