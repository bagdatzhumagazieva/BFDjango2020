from rest_framework import serializers
from django.contrib.auth.models import User
from .models import todoList
# from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class TodoListSerializer(serializers.ModelSerializer):
    # min_count = serializers.IntegerField(default=0)
    count = serializers.IntegerField(read_only=True)

    # username = serializers.CharField(source='created_by.username', read_only=True)

    class Meta:
        model = todoList
        fields = ('id', 'todo', 'done', 'created_by', 'photo', 'file', 'count')

    def validate_todo(self, value):
        if '/' in value:
            raise serializers.ValidationError('invalid char in name field')
        return value


# class RefreshTokenSerializer(serializers.Serializer):
#     refresh = serializers.CharField()
#
#     default_error_messages = {
#         'bad_token': _('Token is invalid or expired')
#     }
#
#     def validate(self, attrs):
#         self.token = attrs['refresh']
#         return attrs
#
#     def save(self, **kwargs):
#         try:
#             RefreshToken(self.token).blacklist()
#         except TokenError:
#             self.fail('bad_token')