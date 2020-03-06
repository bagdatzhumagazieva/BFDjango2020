from rest_framework import serializers
from django.contrib.auth.models import User
from .models import todoList, MyUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email',)

class TodoListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    todo = serializers.CharField(required=True)
    created_by = UserSerializer(read_only=True)
    done = serializers.BooleanField(required=True)

    def create(self, validated_data):
        todo = todoList(**validated_data)
        todo.save()
        return todo

    def update(self, instance, validated_data):
        instance.todo = validated_data.get('todo', instance.todo)
        instance.done = validated_data.get('done', instance.done)
        instance.save()
        return instance

    class Meta:
        model = todoList
        fields = ('id', 'todo', 'done', 'created_by')