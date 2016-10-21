from rest_framework import serializers

from activity.models import Activity
from article.models import Article
from comment.serializers import CommentSerializer
from user.serializers import UserSerializer


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
