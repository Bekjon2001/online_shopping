from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.sellers.choices import SocialLinkType


class Seller(models.Model):
    class Gender(models.TextChoices):
        MALE = _('Male')
        FEMALE = _('Female')

    name = models.CharField(verbose_name=_('Name'),
                            max_length=50
                            )
    rating = models.IntegerField(verbose_name=_('Rating'),
                                 default=0,
                                 validators=[MinValueValidator(0), MaxValueValidator(5)]
                                 )
    male = models.CharField(verbose_name=_('Male'),
                            max_length=10,
                            choices=Gender.choices
                            )

    def __str__(self):
        return self.name


class SellerSocialLink(models.Model):
    social = models.PositiveSmallIntegerField(choices=SocialLinkType.choices)
    social_media = models.URLField(max_length=255, unique=True)

    def __str__(self):
        return self.social_media
