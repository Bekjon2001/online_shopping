from django.core.exceptions import ValidationError
from django.db import models


class About(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField(max_length=255, blank=True)
    image = models.ImageField(upload_to='abouts/images/%Y/%m/%d/')

    def __str__(self):
        return self.title

    def clean(self):
        if not self.pk and About.objects.exists():
            raise ValidationError("About object is already created !")
