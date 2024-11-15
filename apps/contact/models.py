from django.conf import settings
from django.db import models

class Contact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.user:
            self.name, self.email = self.user.first_name, self.user.email
        super().save(*args, **kwargs)
