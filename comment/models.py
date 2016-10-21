from django.db import models

# Create your models here.
from comment.constants import COMMENT_TYPE_CHOICES
from user.models import User


class Comment(models.Model):
    author = models.ForeignKey(User)
    comment_to = models.IntegerField('评论对象id')
    type = models.IntegerField('评论类别', choices=COMMENT_TYPE_CHOICES)
    content = models.TextField('评论内容')
    created_at = models.DateTimeField(auto_now_add=True)
