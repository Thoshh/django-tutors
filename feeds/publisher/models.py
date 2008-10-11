# -*- coding: utf-8 -*-

__revision__ = '$Id$'

from django.db import models

class Entry(models.Model):
    user = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
