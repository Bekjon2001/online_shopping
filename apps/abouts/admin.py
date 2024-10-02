from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import About

@admin.register(About)
class AboutAdmin(TranslationAdmin):
    group_fieldsets = True

    def has_add_permission(self, request, obj=None):
        return not About.objects.exists()

    # fieldsets = (
    #     (
    #         'title',
    #         {'fields':('title',)}
    #
    #     ),
    #     (
    #         ' description',
    #         {'fields':('description',)}
    #     ),
    # )

