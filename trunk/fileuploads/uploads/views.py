# -*- coding: utf-8 -*-

__revision__ = '$Id$'

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from uploads.forms import StaticUploadForm, DynamicUploadForm
from uploads.files import LoggingUploadHandler

def static(request):
    if request.POST:
        static_form = StaticUploadForm(request.POST, request.FILES)
        if static_form.is_valid():
            static_form.save()
            return HttpResponseRedirect(request.path)
    else:
        static_form = StaticUploadForm()
    ctx = {
        'form': static_form,
    }
    return render_to_response('uploads/static.html', ctx,
        context_instance=RequestContext(request))


def dynamic(request):
    if request.POST:
        dynamic_form = DynamicUploadForm(request.POST, request.FILES)
        if dynamic_form.is_valid():
            dynamic_form.save()
            return HttpResponseRedirect(request.path)
    else:
        dynamic_form = DynamicUploadForm()
    ctx = {
        'form': dynamic_form,
    }
    return render_to_response('uploads/dynamic.html', ctx,
        context_instance=RequestContext(request))


def handler(request):
    request.upload_handlers.insert(0, LoggingUploadHandler())
    return static(request)