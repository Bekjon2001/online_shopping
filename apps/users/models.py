from django.contrib.auth.hashers import make_password

from django.contrib.auth.models import AbstractUser, UserManager


from django.db import models

from apps.users.services import user_image_location


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields['is_staff'] = extra_fields['is_superuser'] = True
        return self._create_user(email, password, **extra_fields)



class CustomUser(AbstractUser):

    username = None

    email = models.EmailField(unique=True)
    user_wishlist_count = models.IntegerField(default=0)
    user_cart_count = models.IntegerField(default=0)
    user_image = models.ImageField(
        upload_to= user_image_location,
        blank=True,
        null=True
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


    def __str__(self):
        return self.email


