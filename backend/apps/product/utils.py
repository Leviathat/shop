from django.utils import timezone
import random
import os

def get_image_path():
    now = timezone.now()
    delta = timezone.timedelta(days=30)
    random_timestamp = now - delta * random.random()
    return random_timestamp


def get_product_image_path(instance, filename):
    random_timestamp = get_image_path()
    _, extension = os.path.splitext(filename)
    return os.path.join(f'{str(random_timestamp)}{extension}')

def get_category_image_path(instance, filename):
    random_timestamp = get_image_path()
    _, extension = os.path.splitext(filename)
    return os.path.join(f'{str(random_timestamp)}{extension}')