from django.contrib.auth.models import User
from django.utils import timezone

from mongoengine import Document, EmbeddedDocumentField, EmbeddedDocument
from mongoengine import fields


# Create your models here.
# from app.friend.models import Friend, Waiting, Request, Block
from app.user.functions import return_name_picture
from facefake import settings


def _path_to_avatar(instance, filename):
    return '{user_id}/{dirname}/{filename}'.format(
        user_id=instance.user.id,
        dirname=settings.AVATAR_DIR,
        filename=return_name_picture(filename))


class Friend(EmbeddedDocument):
    # user_id = models.ForeignKey(Profile, related_name='user_id')
    # friend_id = ReferenceField(Profile, reverse_delete_rule=NULLIFY)
    user = fields.IntField()
    create = fields.DateTimeField(default=timezone.now)
    destroy = fields.DateTimeField(default=None)
    status = fields.BooleanField(default=False)


class Waiting(EmbeddedDocument):
    # user_id = models.ForeignKey(Profile, related_name='user_id')
    # waiting_id = ReferenceField(Profile, reverse_delete_rule=NULLIFY)
    user = fields.IntField()
    date = fields.DateTimeField(default=timezone.now)


class Request(EmbeddedDocument):
    # user_id = models.ForeignKey(Profile, related_name='user_id')
    # request_id = ReferenceField(Profile, reverse_delete_rule=NULLIFY)
    user = fields.IntField()
    date = fields.DateTimeField(default=timezone.now)


class Block(EmbeddedDocument):
    # user_id = models.ForeignKey(Profile, related_name='user_id')
    # block_id = ReferenceField(Profile, reverse_delete_rule=NULLIFY)
    user = fields.IntField()
    date = fields.DateTimeField(default=timezone.now)


class Profile(Document):
    user = fields.IntField()
    avatar = fields.ImageField(collection_name='images', size=(6000, 4000, True), thumbnail_size=(400, 400, True),
                               default=None)
    full_name = fields.StringField(max_length=255)
    friend = fields.ListField(EmbeddedDocumentField(Friend))
    waiting = fields.ListField(EmbeddedDocumentField(Waiting))
    request = fields.ListField(EmbeddedDocumentField(Request))
    block = fields.ListField(EmbeddedDocumentField(Block))
