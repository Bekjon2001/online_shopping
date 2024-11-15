from django.utils.timezone import now


def user_image_location(user,file):
    today=now()
    return f'users/{user.get_full_name()}/images/{today.year}/{today.month}/{today.day}/{file}'