from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('todos', views.todo_list)

urlpatterns = router.urls + [
    path('login/', obtain_jwt_token),
    path('todos/<int:pk>/', views.todo_list_detail)
]


