
from django.db.models.signals import post_save
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.contrib import messages
import django_excel as excel
from django import forms
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db import models
from django.template import RequestContext
from django.http import HttpResponseBadRequest
from .models import *
from .forms import BiodataForm, UserRegistrationForm




def user_registration(request):
    form = UserRegistrationForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully registerd')
            return redirect('/preview')
        # If the request params is valid save the data else return form with error
    return render(request, 'registration/registration.html', {'form': form})



# Create your views here.
@login_required()
def index(request):
    return render(request, 'biodata/index.html', {'user': request.user})

@login_required()
def preview(request):
    details = Biodata.objects.all()
    context = {
        'details': details
    }
    return render(request, 'biodata/preview.html', context)

@login_required()
def  history(request):
    return redirect('/admin/')


@login_required()
def add_detail(request):
    if request.method == "POST":
        form = BiodataForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/preview')

    else:
        form = BiodataForm
        return render(request, 'biodata/add_detail.html', {'form':form})


@login_required()
def edit_detail(request, pk):
    detail = get_object_or_404(Biodata, pk=pk)

    if request.method == "POST":
        form = BiodataForm(request.POST, instance = detail)
        if form.is_valid():
            form.save()
            return redirect('/preview')
    else:
        form = BiodataForm(instance = detail)

        return render(request, 'biodata/edit_detail.html', {'form':form})


@login_required()
def delete_detail(request, pk):
    Biodata.objects.filter(id=pk).delete()
    details = Biodata.objects.all()
    context = {
        'details':details
    }
    return render(request, 'biodata/preview.html', context)



def is_valid_form(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid


class UploadFileForm(forms.Form):
    file = forms.FileField()


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


    # return render_to_response('biodata/preview.html',
    #                           {'form': form},
    #                           context_instance=RequestContext(request)
    #                           )

# def download(request):
#     sheet = excel.pe.Sheet([[1, 2],[3, 4]])
#     return excel.make_response(sheet, "xlsx")