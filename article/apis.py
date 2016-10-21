from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from utils.paginations import ArticlePagination
from .models import Article
from .serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    用户个人信息
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny, ]
    pagination_class = ArticlePagination
