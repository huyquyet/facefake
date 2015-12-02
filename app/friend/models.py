# from django.db import models
#
#
# # Create your models here.
# from django.utils import timezone
# from mongoengine import EmbeddedDocument, ReferenceField, DateTimeField, BooleanField, NULLIFY
# from app.user.models import Profile
#
#
# class Friend(EmbeddedDocument):
#     # user_id = models.ForeignKey(Profile, related_name='user_id')
#     friend_id = ReferenceField(Profile, reverse_delete_rule=NULLIFY)
#     create = models.DateTimeField(default=timezone.now)
#     destroy = DateTimeField(default=None)
#     status = BooleanField(default=False)
#
#
# class Waiting(EmbeddedDocument):
#     # user_id = models.ForeignKey(Profile, related_name='user_id')
#     waiting_id = ReferenceField(Profile, reverse_delete_rule=NULLIFY)
#     date = DateTimeField(default=timezone.now)
#
#
# class Request(EmbeddedDocument):
#     # user_id = models.ForeignKey(Profile, related_name='user_id')
#     request_id = ReferenceField(Profile, reverse_delete_rule=NULLIFY)
#     date = DateTimeField(default=timezone.now)
#
#
# class Block(EmbeddedDocument):
#     # user_id = models.ForeignKey(Profile, related_name='user_id')
#     block_id = ReferenceField(Profile, reverse_delete_rule=NULLIFY)
#     date = DateTimeField(default=timezone.now)
