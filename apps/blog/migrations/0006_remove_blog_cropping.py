# Generated by Django 3.1.5 on 2022-03-11 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210522_0740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='cropping',
        ),
    ]