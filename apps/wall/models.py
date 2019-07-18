from __future__ import unicode_literals
from django.db import models
from apps.logreg.models import User
# from apps/logreg/models import User

class Message(models.Model):
    message = models.TextField()
    creator = models.ForeignKey(User, related_name="messages")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.TextField()
    creator = models.ForeignKey(User, related_name="comments")
    parent_message = models.ForeignKey(Message, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
