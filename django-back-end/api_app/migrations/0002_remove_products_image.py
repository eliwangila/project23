# Generated by Django 3.1.13 on 2021-10-27 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='image',
        ),
    ]