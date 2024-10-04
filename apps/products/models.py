from django.db import models
from django.template.defaultfilters import title
from django.utils.translation import gettext_lazy as _

from apps.categories.models import Category
from apps.product_comments.models import ProductComment
from apps.product_ratings.models import ProductRating

CURRENCY_CHOICES = (
    ('USD', 'USD'),
    ('EUR', 'EUR'),
    ('JPY', 'JPY'),
    ("UZS", "UZS"),
)


class Product(models.Model):
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=255
    )
    total_rating = models.DecimalField(
        verbose_name=_('Total Rating'),
        default=0,
        max_digits=10,
        decimal_places=1,
        editable=False
    )
    comment_count = models.IntegerField(
        verbose_name=_('Comment Count'),
        default=0
    )
    price = models.DecimalField(
        verbose_name=_('Price'),
        max_digits=5,
        decimal_places=2,
        default=0
    )
    currency = models.CharField(
        verbose_name=_('Currency'),
        choices=CURRENCY_CHOICES,
        default='USD',
        max_length=5
    )
    short_description = models.CharField(
        verbose_name=_('Short description'),
        max_length=255
    )
    long_description = models.TextField()
    category = models.ForeignKey(
        verbose_name=_('Category'),
        to='categories.Category',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        verbose_name=_('Created Ad'),
        auto_now_add=True
    )
    added_at = models.DateTimeField(
        verbose_name=_('Added at'),
        auto_now_add=True
    )
    main_image = models.ImageField(upload_to='products/images/%Y/%m/%d')

    # def set_total_rating(self):
    #     self.aggregate_amounts = ProductRating.objects.filter(
    #         product_id=self.pk
    #     ).aggregate(
    #         s=models.Sum('rating', default=0),
    #         c=models.Count('id', default=1),
    #     )
    #     self.total_rating = aggregate_amounts['s'] / aggregate_amounts['c']
    #     self.save()

    def set_total_rating(self):
        self.aggregate_amounts = ProductRating.objects.filter(
            product_id=self.pk
        ).aggregate(
            avg=models.Avg('rating', default=0)
        )

        self.total_rating = round(aggregate_amounts['avg'],1)
        self.save()

    def set_comment_count(self):
        self.comment_count = ProductComment.objects.filter(product_id=self.pk).count()
        self.save()

    def __str__(self):
        return self.title
