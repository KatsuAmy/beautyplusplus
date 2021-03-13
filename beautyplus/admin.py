from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Cosmetics

@admin.register(Cosmetics)
class CosmeticsAdmin(ImportExportModelAdmin):
    pass
