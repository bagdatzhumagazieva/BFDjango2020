from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework.views import APIView

from auth_.models import MyUser
from core.serializers import UserSerializer


class registration(APIView):
    def post(self, request):
        password = request.data.get('password')
        username = request.data.get('username')
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        my_user = MyUser.objects.get(username=username)
        my_user.set_password(password)
        my_user.save()
        return Response(serializer.data)
