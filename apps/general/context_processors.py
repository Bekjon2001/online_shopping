

from apps.categories.models import Category
from apps.general.models import General, GeneralSocialMedia
from apps.manufactures.models import Manufacturer


def general_context(request):
    context = {
        'general': General.objects.first(),
        'categories': Category.objects.prefetch_related('children','products').filter(parent__isnull=True),
        'manufactures': Manufacturer.objects.all(),
        'general_social_media': GeneralSocialMedia.objects.all(),
        'currency': request.session.get('currency', General.DEFAULT_CURRENCY),
        'currency_list': General.Currency.labels,
    }
    return context
