import os
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.db.models import ImageField, FileField


@receiver((post_delete, pre_save))
def delete_related_files(instance, sender, **kwargs):
    for field in sender._meta.get_fields():
        if isinstance(field, (ImageField, FileField)):
            file = getattr(instance, field.name)

            if kwargs['signal'] == post_delete:
                if file and os.path.exists(file.path):
                    os.remove(file.path)

            elif kwargs['signal'] == pre_save:
                if instance.pk:
                    old_instance = sender.objects.filter(pk=instance.pk).first()
                    if old_instance:
                        old_file = getattr(old_instance, field.name)
                        if old_file and old_file != file and os.path.exists(old_file.path):
                            os.remove(old_file.path)

