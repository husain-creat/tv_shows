# Generated by Django 2.2.4 on 2023-06-19 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='show',
            name='release_date',
        ),
    ]
