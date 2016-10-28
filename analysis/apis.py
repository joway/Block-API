import datetime

from django.utils.datetime_safe import date
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from analysis.constants import AnalysisQueryTypes
from analysis.serializers import PageViewSerializer, PageViewCreateSerializer, PageViewQuerySerializer
from .models import PageView


class PageViewViewSet(viewsets.GenericViewSet):
    """
    用户个人信息
    """
    queryset = PageView.objects.all()
    serializer_class = PageViewSerializer
    permission_classes = [AllowAny, ]

    def create(self, request, *args, **kwargs):
        serializer = PageViewCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        url = serializer.data['url']
        dt = date.today()
        pv, created = self.queryset.get_or_create(url=url, date=dt)
        pv.count += 1
        pv.save()
        return Response(data=self.get_serializer(pv).data)

    def list(self, request, *args, **kwargs):
        serializer = PageViewQuerySerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        url = serializer.data['url']
        type = serializer.data['type']
        if type == AnalysisQueryTypes.DAILY:
            pvs = self.get_queryset().filter(url=url, date=date.today())
        elif type == AnalysisQueryTypes.WEEKLY:
            pvs = self.get_queryset().filter(date__gte=date.today() - datetime.timedelta(days=7))
        elif type == AnalysisQueryTypes.MONTHLY:
            pvs = self.get_queryset().filter(date__gte=date.today() - datetime.timedelta(days=30))
        elif type == AnalysisQueryTypes.QUARTERLY:
            pvs = self.get_queryset().filter(date__gte=date.today() - datetime.timedelta(days=90))
        elif type == AnalysisQueryTypes.YEARLY:
            pvs = self.get_queryset().filter(date__gte=date.today() - datetime.timedelta(days=365))
        else:
            return Response(data={'detail': 'type 参数错误'}, status=status.HTTP_403_FORBIDDEN)
        return Response(data=self.get_serializer(pvs, many=True).data)
