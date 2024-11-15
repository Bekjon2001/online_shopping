from django.core.exceptions import ValidationError
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category/images/%Y/%m/%d/')
    parent = models.ForeignKey(
        to='self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='children',
        related_query_name='category'
    )
    class Meta:
        verbose_name_plural = "Categories"

    def clean(self):
        try:
            if not self.pk and self.parent.parent:
                raise ValidationError('you can creat only two categories')
        except AttributeError:
            pass


    def __str__(self):
        return self.name
