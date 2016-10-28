from django.db import models


class PageView(models.Model):
    url = models.URLField('链接')
    count = models.IntegerField('点击量', default=0)
    date = models.DateField('日期', auto_now_add=True)
