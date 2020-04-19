from django.db import models
from rest_framework import serializers
from utils.validators import validate_file_size, validate_extension


from auth_.models import MyUser


class todoList(models.Model):
    todo = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='todo_photos',
                              validators=[validate_file_size, validate_extension],
                              null=True, blank=True)
    file = models.FileField(upload_to='todo_files',
                            null=True, blank=True)
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=1)
