# Generated by Django 4.2.1 on 2023-06-01 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_user_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_add',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
