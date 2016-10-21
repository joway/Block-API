from rest_framework import serializers

from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='get_type_display')

    class Meta:
        model = Comment


class CommentQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment_to', 'type')
