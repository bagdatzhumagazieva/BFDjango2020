from rest_framework import serializers
from django.contrib.auth.models import User
from .models import todoList


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class TodoListSerializer(serializers.ModelSerializer):
    min_count = serializers.IntegerField(default=0)
    username = serializers.CharField(source='created_by.username')

    class Meta:
        model = todoList
        fields = ('id', 'todo', 'done', 'created_by', 'photo', 'file', 'count', 'min_count', 'username')
