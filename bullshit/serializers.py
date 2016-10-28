from rest_framework import serializers

from bullshit.models import Bullshit


class BullshitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bullshit


class BullshitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bullshit
        fields = ('content',)
