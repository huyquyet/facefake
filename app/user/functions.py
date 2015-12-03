from django.utils import timezone

__author__ = 'FRAMGIA\nguyen.huy.quyet'

import hashlib


def return_name_picture(filename):
    data = timezone.now()
    name = filename + data
    return hashlib.sha256(name).hexdigest()
