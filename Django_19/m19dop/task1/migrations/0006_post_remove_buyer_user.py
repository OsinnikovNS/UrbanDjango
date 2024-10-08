# Generated by Django 5.0.7 on 2024-08-08 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0005_buyer_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='user',
        ),
    ]
