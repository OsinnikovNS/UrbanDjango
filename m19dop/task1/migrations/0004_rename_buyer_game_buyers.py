# Generated by Django 5.0.7 on 2024-08-01 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0003_alter_buyer_balance_alter_game_cost_alter_game_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='buyer',
            new_name='buyers',
        ),
    ]
