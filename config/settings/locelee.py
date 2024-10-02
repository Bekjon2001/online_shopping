import os
from django.conf import settings

LOCALE_PATHS = [
    os.path.join(settings.BASE_DIR, 'translation'),
]
