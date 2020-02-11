from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
    path('todos/', views.todo_list),
    path('todos/<int:pk>/', views.todo_list_detail)
]