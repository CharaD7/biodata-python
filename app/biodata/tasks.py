# Create your tasks here
from __future__ import absolute_import, unicode_literals
from .celery import shared_task
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, render_to_response, get_object_or_404






class UploadFileForm(forms.Form):
    file = forms.FileField()


@shared_task
# This is the shared task
@login_required()
def upload_detail(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['file']
            return excel.make_response(filehandle.get_sheet(), "xlsx")
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
        context_instance = RequestContext(request)
    return render_to_response('biodata/upload_detail.html',
                              {'form': form},
                              context_instance
                              )