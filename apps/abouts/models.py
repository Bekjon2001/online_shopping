from django.db import models
from django.utils.translation import gettext_lazy as _, get_language
from django.core.exceptions import ValidationError
from django_ckeditor_5.fields import CKEditor5Field


class About(models.Model):
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=255)

    description = models.TextField(
        verbose_name=_('Description'),
        max_length=3000,
        )

    image = models.ImageField(
        verbose_name=_('Image'),
        upload_to='abouts/images/%Y/%m/%d/')

    def __str__(self):
        return self.title
