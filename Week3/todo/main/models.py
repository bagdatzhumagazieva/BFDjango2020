from django.db import models
from django.contrib.auth.models import User

class todoList(models.Model):
    todo = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def to_json(self):
        return {
            'id': self.id,
            'todo': self.todo,
            'done': self.done,
            'created': self.created_by,
        }