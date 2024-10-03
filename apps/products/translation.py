from modeltranslation.translator import TranslationOptions,register

from apps.products.models import Product


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields=('title','price','created_at','added_at',)