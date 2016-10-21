from rest_framework import serializers

from article.models import Article
from comment.serializers import CommentSerializer
from user.serializers import UserSerializer


class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(source='comment_list', many=True)
    author = UserSerializer()
    catalog = serializers.CharField()

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'author', 'catalog', 'tag_list', 'comments')
