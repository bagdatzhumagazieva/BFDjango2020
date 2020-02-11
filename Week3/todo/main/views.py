import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import todoList
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import TodoListSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )

@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data.get('user')
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})

@api_view(['POST'])
def logout(request):
    request.auth.delete()
    return Response(status=status.HTTP_200_OK)

@csrf_exempt
def todo_list(request):
    if request.method == 'GET':
        todos = todoList.objects.all()
        serializer = TodoListSerializer(todos, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = TodoListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors)

@csrf_exempt
def todo_list_detail(request, pk):
    try:
        todo = todoList.objects.get(id=pk)
    except todoList.DoesNotExist as e:
        return todoList(str(e), safe=False)

    if request.method == 'GET':
        serializer = TodoListSerializer(todo)
        return JsonResponse(serializer.data, status=200)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = TodoListSerializer(instance=todo, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        todo.delete()
        return JsonResponse({'deleted': True})