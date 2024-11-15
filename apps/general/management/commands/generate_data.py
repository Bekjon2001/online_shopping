import os


from django.db import transaction

from faker import Faker

from django.conf import settings
from django.utils.timezone import now
from django.core.management import BaseCommand


from apps.abouts.models import About
from apps.categories.models import Category

from apps.general.service import random_image_download
from apps.manufactures.models import Manufacturer
from apps.products.models import Product

fake = Faker()


class Command(BaseCommand):
    @staticmethod
    def generate_about():
        today = now().date()
        if not About.objects.exists():
            django_filename = f'abouts/images/{today.year}/{today.month}/{today.day}/'
            image_dir = os.path.join(settings.MEDIA_ROOT, django_filename)
            image_name = random_image_download(image_dir)
            About.objects.create(
                title=fake.text(155),
                description=fake.text(255),
                image=os.path.join(django_filename, image_name),

            )

    @staticmethod
    def generate_products():
        today = now().date()
        django_filename = f'products/images/{today.year}/{today.month}/{today.day}/'
        image_dir = os.path.join(settings.MEDIA_ROOT, django_filename)

        for cat_i in range(10):
            image_name = random_image_download(image_dir)
            category = Category.objects.create(
                name=fake.first_name(),
                image=os.path.join(django_filename, image_name)
            )
            Manufacturer.objects.create(
                name=fake.first_name(),
                image=os.path.join(django_filename, image_name)
            )

            #============children Category===========
            if cat_i %2 :
                for i in range(3):
                    Category.objects.create(
                        name=fake.last_name(),
                        parent_id=category.pk,
                    )


            products = []
            counts = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
            print(f'Please, Wait for {len(counts) - cat_i} seconds !\n')
            if cat_i + 1 == 1:
                print(f'\t{cat_i + 1} category created ! {(cat_i + 1) * 100} products created !\n')
            else:
                print(f'\t{cat_i + 1} categories created ! {(cat_i + 1) * 100} products created !\n')

            for pro_i in range(100):
                if cat_i in counts:
                    counts.remove(cat_i)
                products.append(
                    Product(
                        title=fake.text(50),
                        short_description=fake.text(255),
                        long_description=fake.text(10_000),
                        category_id=category.pk,
                        main_image=os.path.join(django_filename, image_name),


                    )
                )
            Product.objects.bulk_create(products)

    @transaction.atomic
    def handle(self, *args, **options):
        # ====================== generate about model ======================
        print(self.stdout.write(self.style.SUCCESS('Successfully generated about data')))
        self.generate_about()

        # ====================== generate product model ======================
        print(self.stdout.write(self.style.SUCCESS('Successfully generated products data')))
        self.generate_products()
        print(self.stdout.write(self.style.SUCCESS('Done')))
