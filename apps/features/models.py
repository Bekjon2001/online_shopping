from django.db import models


class Feature(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class FeatureValue(models.Model):
    feature = models.ForeignKey('features.Feature', on_delete=models.PROTECT, related_name='feature_values')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = (('feature', 'name'),)
