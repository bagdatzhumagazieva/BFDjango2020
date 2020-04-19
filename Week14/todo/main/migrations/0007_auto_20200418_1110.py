# Generated by Django 2.2 on 2020-04-18 11:10

from django.db import migrations, models
import utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200418_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='todo_photos', validators=[utils.validators.validate_file_size, utils.validators.validate_extension]),
        ),
    ]
