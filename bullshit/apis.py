from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from bullshit.serializers import BullshitSerializer, BullshitCreateSerializer
from .models import Bullshit


class BullshitViewSet(viewsets.ModelViewSet):
    """
    用户个人信息
    """
    queryset = Bullshit.objects.all()
    serializer_class = BullshitSerializer
    permission_classes = [AllowAny, ]

    def create(self, request, *args, **kwargs):
        serializer = BullshitCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
