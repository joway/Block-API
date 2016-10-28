from django.db import models

import comment.services
from activity.services import ActivityService
from user.models import User
from utils.constants import CONTENT_TYPE_CHOICES, ContentTypes


class Comment(models.Model):
    author = models.ForeignKey(User)
    comment_to = models.IntegerField('评论对象id')
    type = models.IntegerField('评论类别', choices=CONTENT_TYPE_CHOICES)
    content = models.TextField('评论内容')
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def target(self):
        return comment.services.CommentService.get_target(comment_to=self.comment_to, type=self.type)

    def save(self, *args, **kwargs):
        super(...).save(*args, **kwargs)
        ActivityService.create_activity(user=self.author, obj=self, type=ContentTypes.COMMENT)
