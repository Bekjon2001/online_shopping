from django import forms
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model

from apps.users.models import CustomUser


class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(
        max_length=150,
        min_length=3,
        required=True,
    )
    email = forms.EmailField(
        required=True,
    )
    password = forms.CharField(
        min_length=8,
        required=True,
        validators=[validate_password],
    )


    def clean_username(self):
        username = self.cleaned_data['first_name']
        kwargs={
            CustomUser.USERNAME_FIELD: username,
        }
        if get_user_model().objects.filter(**kwargs).exists():
            raise forms.ValidationError('Username already exists')
        return username


