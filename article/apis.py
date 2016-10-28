from rest_framework import viewsets, status
from rest_framework.decorators import list_route
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

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

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(is_post=True)
        page = self.paginate_queryset(queryset=queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    @list_route(methods=['GET'])
    def about(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(is_post=False, title__contains='About').first()
        return Response(self.get_serializer(queryset).data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
