from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('todos/', views.TodoList.as_view()),
    path('todos/<int:pk>/', views.TodoDetail.as_view()),
]
