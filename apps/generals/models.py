from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from .validation_phone import validate_phone


class General(models.Model):
    phone1 = models.CharField(verbose_name=_('Phone1'),
                              max_length=13,
                              validators=[validate_phone],
                              help_text="UZB Number +998123456789"
                              )
    phone2 = models.CharField(verbose_name=_('Phone2'),
                              max_length=13,
                              null=True,
                              blank=True,
                              validators=[validate_phone]
                              )

    location = models.URLField()
    address = models.CharField(verbose_name=_('Address'),
                               max_length=100,
                               null=True,
                               blank=True
                               )
    logo = models.ImageField(verbose_name=_('Logo'),
                             upload_to="generals/logo/image/%Y/%m/%d/"
                             )

    def clean(self):
        if self.pk and General.objects.exists():
            raise ValidationError('Unique')


class GeneralSocialMedia(models.Model):
    url = models.URLField()
    icon = models.ImageField(verbose_name=_('Icon'),
                             upload_to="social_links/icon/image/%Y/%m/%d/"
                             )
