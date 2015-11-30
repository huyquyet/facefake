# from django.contrib.auth.models import User
# from django.db import models
#
#
# # Create your models here.
# from django.utils import timezone
# from app.user.functions import return_name_picture
# from facefake import settings
#
#
# def _path_to_avatar(instance, filename):
#     return '{user_id}/{dirname}/{filename}'.format(
#         user_id=instance.user.id,
#         dirname=settings.AVATAR_DIR,
#         filename=return_name_picture(filename))
#
#
# class Profile(models.Model):
#     user = models.OneToOneField(User, related_name='profile')
#     avatar = models.ImageField(upload_to=_path_to_avatar, blank=True, max_length=255)
#     friend = models.ManyToManyField('self', through='Friend', through_fields=('user_id', 'friend_id'),
#                                     related_name='friends', symmetrical=False)
#     waiting = models.ManyToManyField('self', through='Waiting', through_fields=('user_id', 'waiting_id'),
#                                      symmetrical=False)
#     request = models.ManyToManyField('self', through='Request', through_fields=('user_id', 'request_id'),
#                                      symmetrical=False)
#     block = models.ManyToManyField('self', through='Block', through_fields=('user_id', 'block_id'),
#                                    symmetrical=False)
#
#
# class Friend(models.Model):
#     user_id = models.ForeignKey(Profile, related_name='user_id')
#     friend_id = models.ForeignKey(Profile, related_name='friend_id')
#     create = models.DateTimeField(default=timezone.now)
#     destroy = models.DateTimeField(default=None)
#     status = models.BooleanField(default=False)
#
#
# class Waiting(models.Model):
#     user_id = models.ForeignKey(Profile, related_name='user_id')
#     waiting_id = models.ForeignKey(Profile, related_name='waiting_id')
#     date = models.DateTimeField(default=timezone.now)
#
#
# class Request(models.Model):
#     user_id = models.ForeignKey(Profile, related_name='user_id')
#     request_id = models.ForeignKey(Profile, related_name='request_id')
#     date = models.DateTimeField(default=timezone.now)
#
#
# class Block(models.Model):
#     user_id = models.ForeignKey(Profile, related_name='user_id')
#     block_id = models.ForeignKey(Profile, related_name='block_id')
#     date = models.DateTimeField(default=timezone.now)

