from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from comment.serializers import CommentSerializer, CommentQuerySerializer, CommentCreateSerializer
from .models import Comment


class CommentViewSet(viewsets.GenericViewSet):
    """
    用户个人信息
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny, ]

    def create(self, request, *args, **kwargs):
        serializer = CommentCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)

        return Response(data={'detail': '评论创建成功'})

    def list(self, request, *args, **kwargs):
        serializer = CommentQuerySerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        data = serializer.data

        comments = self.get_queryset().filter(comment_to=data['comment_to'], type=data['type'])
        comments_serializer = self.get_serializer(comments, many=True)
        return Response(comments_serializer.data)
