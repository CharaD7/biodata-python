from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Employee


# Register your models here.
@admin.register(Employee)

class EmployeeAdmin(ImportExportModelAdmin):
    """
        This is to allow admin upload excel files of biodata
    """
    pass