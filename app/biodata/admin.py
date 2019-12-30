from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Biodata, UserProfile


# Register your models here.
@admin.register(Biodata)
@admin.register(UserProfile)
# admin.site.register(UserProfile)

class BiodataAdmin(ImportExportModelAdmin):
    pass