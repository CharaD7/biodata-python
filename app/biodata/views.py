import csv, io
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.contrib import messages
# from django.contrib.auth.decorators import permission_required



from .models import *
from .forms import BiodataForm
from .tasks import upload_detail

# Create your views here.
def index(request):
    return render(request, 'biodata/index.html')

def preview(request):
    details = Biodata.objects.all()
    context = {
        'details': details
    }
    return render(request, 'biodata/preview.html', context)

def  history(request):
    return redirect('/admin/')



def add_detail(request):
    if request.method == "POST":
        form = BiodataForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/preview')

    else:
        form = BiodataForm
        return render(request, 'biodata/add_detail.html', {'form':form})

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

def delete_detail(request, pk):
    Biodata.objects.filter(id=pk).delete()
    details = Biodata.objects.all()
    context = {
        'details':details
    }
    return render(request, 'biodata/preview.html', context)


upload_detail.delay(request)