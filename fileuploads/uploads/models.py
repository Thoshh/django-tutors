# -*- coding: utf-8 -*-

from django.db import models

class StaticFileUpload(models.Model):
    upload = models.FileField('upload', upload_to='uploads/files')
    title = models.CharField('title', max_length=100)

    def __unicode__(self):
        return self.title