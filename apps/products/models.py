from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from apps.categories.models import Category
from apps.comments.models import ProductComment
from apps.general.models import General


class Product(models.Model):
    title = models.CharField(max_length=155)
    price = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        editable=False,
        default=Decimal(0),
        help_text='Enter in UZS'
    )
    old_price = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        editable=False,
        help_text='Enter in UZS',
        default=Decimal(0)
    )
    avg_rating = models.DecimalField(
        max_digits=10,
        decimal_places=1,
        default=Decimal('0'),
        editable=False
    )
    comments_count = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        default=Decimal('0'),
        editable=False
    )
    seen_count = models.PositiveBigIntegerField(default=0)
    short_description = models.CharField(max_length=255)
    long_description = models.TextField(max_length=10_000, blank=True)
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    added_at = models.DateTimeField(auto_now=True)
    main_image = models.ImageField(upload_to='products/images/%Y/%m/%d/')


    @property
    def features(self):
        product_features = ProductFeature.objects.prefetch_related('feature_values').filter(product_id=self.pk)
        features = {}
        for product_feature in product_features:
            for value in product_feature.feature_values.all():
                if value.feature_id not in features:
                    features[value.feature_id] = {
                        'id': value.feature_id,
                        'name': value.feature.name,
                        'values': [
                            {'id': value.id, 'name': value.name},
                        ]
                    }
                else:
                    features[value.feature_id]['values'].append({'id': value.id, 'name': value.name})
        return list(features.values())

    def set_avg_rating(self):
        aggregated_amount = ProductComment.objects.filter(
            product_id=self.pk
        ).aggregate(
            avg=models.Avg('rating', default=0),
        )
        self.avg_rating = round(aggregated_amount['avg'], 1)
        self.save()

    def set_comments_rating(self):
        self.comments_count = ProductComment.objects.filter(product_id=self.pk).count()
        self.save()





class ProductImage(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product/images/%Y/%m/%d/')
    ordering_number = models.PositiveSmallIntegerField(default=0)


class ProductFeature(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='product_features')
    feature_values = models.ManyToManyField('features.FeatureValue')
    price = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text='Enter in UZS',
        null=True
    )
    old_price = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text='Enter in UZS',
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.product.price, self.product.old_price = self.price, self.old_price
        self.product.save()

