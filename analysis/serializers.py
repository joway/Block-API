from rest_framework import serializers

from analysis.models import PageView


class PageViewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageView
        fields = ('url',)


class PageViewQuerySerializer(serializers.ModelSerializer):
    type = serializers.CharField()

    class Meta:
        model = PageView
        fields = ('url', 'type')


class PageViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageView
