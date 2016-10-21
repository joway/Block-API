from django.db import models
from taggit.managers import TaggableManager

from catalog.models import Catalog
from comment.constants import CommentTypes
from comment.models import Comment
from user.models import User


class Article(models.Model):
    title = models.CharField('标题', max_length=255)
    author = models.ForeignKey(verbose_name='用户', to=User)
    content = models.TextField('Markdown 文本')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now_add=True)

    tags = TaggableManager(blank=True)

    catalog = models.ForeignKey(verbose_name='目录', to=Catalog)

    def tag_list(self):
        return [o.name for o in self.tags.all()]

    def comment_list(self):
        return Comment.objects.filter(comment_to=self.id, type=CommentTypes.ARTICLE)
