from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, AbstractUser

from .models import todoList, Profile


# @admin.register(User)
# class MyUserAdmin(UserAdmin):
#     list_display = ('id', 'username', 'email', 'first_name', 'last_name')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bio', 'address',)


@admin.register(todoList)
class TodoList(admin.ModelAdmin):
    list_display = ('id', 'todo', 'done', 'created_by', 'photo', 'file')