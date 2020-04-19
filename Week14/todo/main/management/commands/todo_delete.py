from django.core.management.base import BaseCommand
import datetime
from main.models import todoList


def create_todos(num=3):
    todos = [todoList(todo=f'todo {i}',
                      done=False) for i in range(num)]

    todoList.objects.bulk_create(todos)


class Command(BaseCommand):
    help = 'Delete Toto objects from Todo table'

    def add_arguments(self, parser):
        parser.add_argument('todo_ids', nargs='+', help='Todo ids for delete')

    def handle(self, *args, **kwargs):

        for todo_id in kwargs['todo_ids']:
            try:
                b = todoList.objects.get(id=todo_id)
                b.delete()
                self.stdout.write(self.style.SUCCESS(f"Todo id: {todo_id} was deleted successfully"))
            except todoList.DoesNotExist as e:
                self.stdout.write(self.style.ERROR(f"Todo id: {todo_id} does not exists!"))
