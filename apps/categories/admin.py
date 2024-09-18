from django.contrib import admin

from apps.categories.models import Category

from apps.categories.filters import CategoryFilter


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_uz','name_ru','name_en')
    search_fields = ('name_uz', 'name_ru', 'name_en')


