from django.db import models

from activity.services import ActivityService
from user.models import User
from utils.constants import ContentTypes


class Bullshit(models.Model):
    author = models.ForeignKey(User)
    content = models.TextField('闲扯内容')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super(...).save(*args, **kwargs)
        ActivityService.create_activity(user=self.author, obj=self, type=ContentTypes.BULLSHIT)
