# Generated by Django 2.2 on 2020-04-18 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200418_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='todo_files'),
        ),
    ]