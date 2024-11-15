from django.core.validators import RegexValidator

check_uzb_number = RegexValidator(
    regex=r'^\+998\d{9}$',
    message='Invalid phone number format. A valid number starts with +998 followed by 9 digits.',
    code='invalid_number'
)


