from django.core.management.base import BaseCommand
import datetime
from main.models import todoList


def create_todos(num=3):
    todos = [todoList(todo=f'todo {i}',
                      done=False) for i in range(num)]

    todoList.objects.bulk_create(todos)


class Command(BaseCommand):
    help = 'Create fake data for Todo table'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Number of todos for creation')

        parser.add_argument('-p', '--prefix', type=str, help='Prefix string for new todos')

    def handle(self, *args, **kwargs):
        # todoList.objects.all().delete()
        total = kwargs['total']
        prefix = kwargs.get('prefix')
        if not prefix:
            prefix = 'AA'
        self.stdout.write(kwargs.get('prefix'))
        # for i in range(total):
        #     t = todoList.objects.create(todo=f'todo {prefix}', done=True)
        #     self.stdout.write(f'book{t.id} was created')
        # create_todos(total)

        create_todos(total)