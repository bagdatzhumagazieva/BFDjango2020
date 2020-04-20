from django.core.management.base import BaseCommand
from main.models import todoList


def create_todos(num=3, prefix=''):
    todos = [todoList(todo=f'todo {prefix}',
                      done=False, )
               for i in range(num)]

    todoList.objects.bulk_create(todos)


class Command(BaseCommand):
    help = 'Create fake date for Todo table'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Number of todos for creation')

        parser.add_argument('-p', '--prefix', type=str, help='Prefix string for new todos')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        prefix = kwargs.get('prefix')

        if not prefix:
            prefix = 'Bagdat'

        create_todos(total, prefix)