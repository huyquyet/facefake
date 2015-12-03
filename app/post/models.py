from django.utils import timezone
from mongoengine import Document
from mongoengine import fields


# Create your models here.

class Comment(fields.EmbeddedDocument):
    created_at = fields.DateTimeField(default=timezone.now, required=True)
    author = fields.StringField(verbose_name="Name", max_length=255, required=True)
    body = fields.StringField(verbose_name="Comment", required=True)

    class Meta:
        app_label = 'no_sql'


class Post(Document):
    created_at = fields.DateTimeField(default=timezone.now, required=True)
    title = fields.StringField(max_length=255, required=True)
    slug = fields.StringField(max_length=255, required=True, primary_key=True)
    comments = fields.ListField(fields.EmbeddedDocumentField('Comment'))

    class Meta:
        app_label = 'no_sql'
