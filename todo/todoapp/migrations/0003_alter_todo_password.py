# Generated by Django 5.0.6 on 2024-05-17 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_rename_text_todo_email_todo_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='password',
            field=models.IntegerField(),
        ),
    ]
