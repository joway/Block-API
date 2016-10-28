import article.models
from comment.models import Comment
from utils.constants import ContentTypes


class CommentService(object):
    @classmethod
    def get_target(cls, comment_to, type):
        if type == ContentTypes.ARTICLE:
            obj = article.models.Article.objects.get(id=comment_to)
        else:
            raise Exception('无效评论')
        return obj

    @classmethod
    def get_comments(cls, comment_to, type):
        return Comment.objects.filter(comment_to=comment_to, type=type)
