# -*- coding: utf-8 -*-

__revision__ = '$Id$'

from django.contrib import admin

from uploads import models


class StaticUploadAdmin(admin.ModelAdmin):
    save_on_top = True


class DynamicUploadAdmin(admin.ModelAdmin):
    save_on_top = True


admin.site.register(models.StaticFileUpload, StaticUploadAdmin)
admin.site.register(models.DynamicFileUpload, DynamicUploadAdmin)