# -*- coding: utf-8 -*-

__revision__ = '$Id$'

from django.db import models

### upload to static path ###
class StaticFileUpload(models.Model):
    upload = models.FileField('upload', upload_to='uploads/files')
    title = models.CharField('title', max_length=100)

    def __unicode__(self):
        return self.title

### upload to dynamic path ###
def get_dynamic_path(instance, filename):
    """Bit of stupidity: the dynamic element is determined by length of title"""
    return 'dynamic/%s/file/%s' % (str(len(instance.title)), filename)

class DynamicFileUpload(models.Model):
    upload = models.FileField('upload', upload_to=get_dynamic_path)
    title = models.CharField('title', max_length=100)

    def __unicode__(self):
        return self.title