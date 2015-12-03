from django.contrib.auth.models import User



# Create your models here.
# from app.friend.models import Friend, Waiting, Request, Block


# def _path_to_avatar(instance, filename):
#     return '{user_id}/{dirname}/{filename}'.format(
#         user_id=instance.user.id,
#         dirname=settings.AVATAR_DIR,
#         filename=return_name_picture(filename))
from django.utils import timezone
from mongoengine import Document
from mongoengine.fields import EmbeddedDocument, IntField, DateTimeField, BooleanField, ImageField, StringField, \
    ListField, EmbeddedDocumentField


class Friend(EmbeddedDocument):
    # user_id = models.ForeignKey(Profile, related_name='user_id')
    # friend_id = ReferenceField(Profile, reverse_delete_rule=NULLIFY)
    user = IntField()

    create = DateTimeField(default=timezone.now)
    destroy = DateTimeField(default=None)
    status = BooleanField(default=False)

    class Mete:
        app_label = 'no_sql'


class Waiting(EmbeddedDocument):
    # user_id = models.ForeignKey(Profile, related_name='user_id')
    # waiting_id = ReferenceField(Profile, reverse_delete_rule=NULLIFY)
    user = IntField()
    date = DateTimeField(default=timezone.now)

    class Mete:
        app_label = 'no_sql'


class Request(EmbeddedDocument):
    # user_id = models.ForeignKey(Profile, related_name='user_id')
    # request_id = ReferenceField(Profile, reverse_delete_rule=NULLIFY)
    user = IntField()
    date = DateTimeField(default=timezone.now)

    class Mete:
        app_label = 'no_sql'


class Block(EmbeddedDocument):
    # user_id = models.ForeignKey(Profile, related_name='user_id')
    # block_id = ReferenceField(Profile, reverse_delete_rule=NULLIFY)
    user = IntField()
    date = DateTimeField(default=timezone.now)

    class Mete:
        app_label = 'no_sql'


class Profile(Document):
    # user = IntField()
    _id = IntField()
    avatar = ImageField(collection_name='images', size=(6000, 4000, True), thumbnail_size=(400, 400, True),
                        default=None)
    full_name = StringField(max_length=255)
    other_name = StringField(max_length=255)
    friend = ListField(EmbeddedDocumentField(Friend))
    waiting = ListField(EmbeddedDocumentField(Waiting))
    request = ListField(EmbeddedDocumentField(Request))
    block = ListField(EmbeddedDocumentField(Block))

    class Meta:
        app_label = 'no_sql'
