import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import todoList, MyUser
from .serializers import UserSerializer
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from .serializers import TodoListSerializer


class UserList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TodoList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = todoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TodoDetail(mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset = todoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


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
