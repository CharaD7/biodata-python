from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Biodata


# Register your models here.
@admin.register(Biodata)

class BiodataAdmin(ImportExportModelAdmin):
    pass