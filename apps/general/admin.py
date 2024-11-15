from django.contrib import admin

from apps.general.models import General


@admin.register(General)
class GeneralAdmin(admin.ModelAdmin):
    pass
