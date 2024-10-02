from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name= models.CharField(
        verbose_name=_('Name'),
        max_length=255, )

    parent = models.ForeignKey(
        'self',
        verbose_name=_('Parent UZ'),
        null=True,
        blank=True,
        related_name='children_uz',
        on_delete=models.CASCADE)

    def clean(self):
        try:
            if not self.pk and self.parent.parent.parent:
                raise ValidationError('you can creat only three category')
        except AttributeError:
            pass


    def __str__(self):
        return self.name
