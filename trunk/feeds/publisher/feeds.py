# -*- coding: utf-8 -*-

__revision__ = '$Id$'

from django.contrib.syndication.feeds import Feed
from django.utils.feedgenerator import Atom1Feed

from publisher.models import Entry


class UserEntriesFeed(Feed):
    feed_type = Atom1Feed

    def get_object(self, bits):
        return bits[0]

    def items(self, obj):
        return Entry.objects.filter(user=obj)[:10]

    def link(self, obj):
        return '/'

    def item_link(self, obj):
        return '/entries/%s/' % obj.pk

    def title(self, obj):
        return obj
