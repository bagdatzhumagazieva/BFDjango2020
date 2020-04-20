from rest_framework import serializers
from django.contrib.auth.models import User
from .models import todoList


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)

    def validate_password(self, password):
        if len(password) < 5:
            raise serializers.ValidationError('It is too short password')
        return password


class TodoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = todoList
        fields = ('id', 'todo', 'done', 'created_by', 'photo', 'file')
