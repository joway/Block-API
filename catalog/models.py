from django.db import models

# Create your models here.
from utils.constants import CONTENT_TYPE_CHOICES


class Catalog(models.Model):
    name = models.CharField('目录名', max_length=255)
    type = models.IntegerField(choices=CONTENT_TYPE_CHOICES)

    def __str__(self):
        return self.name
