from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

from api.views_sets import CategoryViewSet, ProductxViewSet
from .views import CategoryListAPIView, CategoryDetailAPIView

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('category/', CategoryListAPIView.as_view()),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view()),
]