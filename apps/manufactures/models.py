from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category/images/%Y/%m/%d/')

    def __str__(self):
        return self.name
