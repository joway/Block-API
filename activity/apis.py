from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Activity
from .serializers import ActivitySerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """
    用户个人信息
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [AllowAny, ]
