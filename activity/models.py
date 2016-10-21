from django.db import models

# Create your models here.
from activity.constants import ACTIVITY_TYPE_CHOICES
from user.models import User


class Activity(models.Model):
    target = models.CharField('活动对象', max_length=1024)
    owner = models.ForeignKey(User)
    created_at = models.DateTimeField('创建时间')
    type = models.IntegerField('活动种类', choices=ACTIVITY_TYPE_CHOICES)
