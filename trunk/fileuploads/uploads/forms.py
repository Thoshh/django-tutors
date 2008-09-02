# -*- coding: utf-8 -*-

__revision__ = '$Id$'

from django import forms

from uploads.models import StaticFileUpload, DynamicFileUpload

class StaticUploadForm(forms.Form):
    upload = forms.FileField(label='file')
    title = forms.CharField(label='title')

    def save(self):
        upload = StaticFileUpload(title=self.cleaned_data['title'])
        data = self.cleaned_data['upload']
        upload.upload.save(data.name, data)
        return upload


class DynamicUploadForm(forms.Form):
    upload = forms.FileField(label='file')
    title = forms.CharField(label='title')

    def save(self):
        upload = DynamicFileUpload(title=self.cleaned_data['title'])
        data = self.cleaned_data['upload']
        upload.upload.save(data.name, data)
        return upload