# Generated by Django 5.0.6 on 2024-05-18 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_alter_todo_email_alter_todo_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='Name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todo',
            name='Email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todo',
            name='password',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
