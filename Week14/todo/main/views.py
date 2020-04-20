import logging
import json

from django.db.models import Avg, Max, Min, Sum, Count
from rest_framework import viewsets
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

from .models import todoList
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from .serializers import TodoListSerializer

logger = logging.getLogger(__name__)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class registration(APIView):
    def post(self, request):
        password = request.data.get('password')
        username = request.data.get('username')
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        my_user = User.objects.get(username=username)
        my_user.set_password(password)
        my_user.save()
        return Response(serializer.data)


@api_view(['POST'])
def logout(request):
    request.auth.delete()
    return Response(status=status.HTTP_200_OK)

class todo_list(viewsets.ModelViewSet):
    # queryset = todoList.objects.annotate(min_count=Count(count))
    queryset = todoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = (IsAuthenticated,)
    parser_classes = (FormParser, MultiPartParser, JSONParser)

    # def get_queryset(self):
    #     if self.action == 'list':
    #         return todoList.objects.select_related('done')
    #     return todoList.objects.all()

    def perform_create(self, serializer):
        serializer.save()
        logger.debug(f'Todo is created ID: {serializer.instance}')
        logger.info(f'Todo is created ID: {serializer.instance}')
        logger.warning(f'Todo is created ID: {serializer.instance}')
        logger.error(f'Todo is created ID: {serializer.instance}')
        logger.critical(f'Todo is created ID: {serializer.instance}')

    @action(methods=['GET'], detail=False)
    def check_count(self, request):
        data = [
            todoList.objects.aggregate(Avg('count')),
            todoList.objects.aggregate(max_price=Max('count')),
            todoList.objects.aggregate(Min('count')),
            todoList.objects.aggregate(Sum('count')),
            # Author.objects.values('id').annotate(Count('books'))
        ]
        return Response(data)


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
