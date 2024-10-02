from django.conf import settings
from django.utils.translation import gettext_lazy as _

LANGUAGE_CODE = 'en'
LOCALE_PATHS = [
    settings.BASE_DIR / 'translations'
]

USE_I18N = True

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'

gettext = lambda s: s
LANGUAGES = (
    ('en', _('English')),
    ('uz', _('Uzbek')),
    ('ru', _('Russian')),
)
MODELTRANSLATION_LANGUAGES = ('en','uz','ru')