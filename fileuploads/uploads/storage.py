# -*- coding: utf-8 -*-

__revision__ = '$Id$'

from django.core.files.storage import Storage


class PickledDictStorage(Storage):

    def _open(self, name, mode='rb'):
        pass

    def _save(self, name, content):
        pass