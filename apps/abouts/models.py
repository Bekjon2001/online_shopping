from django.db import models
from django.utils.translation import gettext_lazy as _, get_language
from django.core.exceptions import ValidationError
from django_ckeditor_5.fields import CKEditor5Field


class About(models.Model):
    title_uz = models.CharField(verbose_name=_('Title UZ'), max_length=255, default='')
    title_ru = models.CharField(verbose_name=_('Title RU'), max_length=255, default='')
    title_en = models.CharField(verbose_name=_('Title EN'), max_length=255, default='')
    description_uz = CKEditor5Field(verbose_name=_('Description UZ'), max_length=3000, default='')
    description_ru = CKEditor5Field(verbose_name=_('Description RU'), max_length=3000, default='')
    description_en = CKEditor5Field(verbose_name=_('Description EN'), max_length=3000, default='')
    image = models.ImageField(verbose_name=_('Image'), upload_to='abouts/images/%Y/%m/%d/')

    def title(self):
        # Get the language code, stripping any region part
        lang_code = get_language().split('-')[0]
        # Return the corresponding title, default to an empty string if not found
        return getattr(self, f'title_{lang_code}', '')

    def description(self):
        # Get the language code, stripping any region part
        lang_code = get_language().split('-')[0]
        # Return the corresponding title, default to an empty string if not found
        return getattr(self, f'description_{lang_code}', '')

    def clean(self):
        if not self.pk and About.objects.exists():
            raise ValidationError("About object is already created")

    def save(self, *args, **kwargs):
        if self.title_uz:
            self.title_uz = ' '.join(self.title_uz.split())
        if self.description_uz:
            self.description_uz = ' '.join(self.description_uz.split())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
