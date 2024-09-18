from django.contrib import admin
from .models import About

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'title_ru', 'title_en', 'image')
    search_fields = ('title_uz', 'title_ru', 'title_en')
