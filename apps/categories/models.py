from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _, get_language


class Category(models.Model):
    name_uz = models.CharField(verbose_name=_('Name UZ'),
                               max_length=255,
                               default=''
                               )
    name_ru = models.CharField(verbose_name=_('Name RU'),
                               max_length=255,
                               default=''
                               )
    name_en = models.CharField(verbose_name=_('Name EN'),
                               max_length=255,
                               default=''
                               )
    parent_uz = models.ForeignKey('self',
                                  verbose_name=_('Parent UZ'),
                                  null=True,
                                  blank=True,
                                  related_name='children_uz',
                                  on_delete=models.CASCADE
                                  )
    parent_ru = models.ForeignKey('self',
                                  verbose_name=_('Parent RU'),
                                  null=True,
                                  blank=True,
                                  related_name='children_ru',
                                  on_delete=models.CASCADE
                                  )
    parent_en = models.ForeignKey('self',
                                  verbose_name=_('Parent EN'),
                                  null=True,
                                  blank=True,
                                  related_name='children_en',
                                  on_delete=models.CASCADE
                                  )

    @property
    def name(self):
        lang = get_language().split('-')[0]
        return getattr(self, f'name_{lang}', '')

    @property
    def description(self):
        lang = get_language()
        return getattr(self, f'description_{lang}', '')

    def clean(self):
        try:
            if not self.pk and self.parent.parent.parent:
                raise ValidationError('you can creat only three category')
        except AttributeError:
            pass

    # def category_filter(self):
    #     if self.parent is None:
    #         return self.name
    #     elif self.parent.parent is not None and self.children:
    #         return self.name
    #     elif self.parent.parent is not None and self.children is None:
    #         return self.name

    def __str__(self):
        return self.name
