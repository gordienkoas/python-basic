# Generated by Django 4.2.3 on 2023-11-03 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0004_myuser_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='avatar',
        ),
    ]
