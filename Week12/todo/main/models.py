from django.db import models
from django.contrib.auth.models import User

from utils.validators import validate_file_size, validate_extension


class todoList(models.Model):
    todo = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='todo_photos',
                              validators=[validate_file_size, validate_extension],
                              null=True, blank=True)
    file = models.FileField(upload_to='todo_files',
                            null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return '{}: {}, {}, {}, {}, {}'.format(self.id, self.todo, self.done, self.created_by, self.photo, self.file)

    def to_json(self):
        return {
            'id': self.id,
            'todo': self.todo,
            'done': self.done,
            'created': self.created_by,
        }
