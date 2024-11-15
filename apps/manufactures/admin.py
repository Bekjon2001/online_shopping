from django.contrib import admin

from apps.manufactures.models import Manufacturer


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass
