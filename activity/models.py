from django.db import models

from user.models import User
from utils.constants import CONTENT_TYPE_CHOICES


class Activity(models.Model):
    owner = models.ForeignKey(User)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    type = models.IntegerField('活动种类', choices=CONTENT_TYPE_CHOICES)
    description = models.CharField('活动内容', max_length=1024)
