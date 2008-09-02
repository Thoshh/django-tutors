# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from uploads.forms import FileUploadForm

def index(request):
    if request.POST:
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    else:
        form = FileUploadForm()
    ctx = {
        'form': form,
    }
    return render_to_response('uploads/index.html', ctx,
        context_instance=RequestContext(request))