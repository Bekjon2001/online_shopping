from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def decimal_to_range(context, decimal_number):
    try:
        # Bo'sh yoki noto'g'ri qiymatni tekshirish
        decimal_value = int(decimal_number)
        return range(decimal_value)
    except (ValueError, TypeError):
        # Agar qiymat bo'sh yoki noto'g'ri bo'lsa, default qiymat sifatida bo'sh range qaytaramiz
        return range(0)

@register.simple_tag(takes_context=True)
def normalize_date(context,date_obj):
    return date_obj.strftime('%d.%m.%Y')