# Generated by Django 4.2.1 on 2023-06-01 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_created_add'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created_add',
        ),
    ]