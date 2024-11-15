from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from apps.categories.models import Category
from apps.categories.filters import CategoryFilter


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_filter = (CategoryFilter,)
