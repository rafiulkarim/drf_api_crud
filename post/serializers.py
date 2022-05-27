from asyncore import read
from dataclasses import field
from rest_framework import serializers 

from .models import *


class PostSerializer(serializers.ModelSerializer):
    my_comments = serializers.SerializerMethodField(read_only=True)

    def get_my_comments(self, obj):
        try:
            instance = Comment.objects.get(post_id=obj.id)
            return CommentSerializer(instance).data
        except Comment.DoesNotExist:
            raise Http404

    class Meta:
        model = Post
        fields = [
            'title',
            'description',
            'my_comments',
        ]


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'content',
            'post',
        ]



