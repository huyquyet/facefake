from django.dispatch import receiver
from mongo_auth.models import User
from mongoengine import post_save

__author__ = 'FRAMGIA\nguyen.huy.quyet'


# @receiver(post_save, sender=User)