# Generated by Django 5.1 on 2024-08-09 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0008_rename_created_post_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
