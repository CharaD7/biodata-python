from __future__ import absolute_import, unicode_literals

# Create your tasks here
import csv, io
from django.shortcuts import render
from django.contrib import messages

from celery import shared_task


from .models import *



@shared_task
def upload_detail(request):
    for column in csv.reader(io_string, delimiter = ',', quotechar = '|'):
        # _, allows us to skip the .save() call
        _, created = Biodata.objects.update_or_create(
            firstname = column[0],
            lastname = column[1],
            age = column[2],
            gender = column[3],
            address = column[4],
            date_of_birth = column[5],
            email = column[6]
        )
        context = {}
        return render(request, 'biodata/preview.html', context, prompt)