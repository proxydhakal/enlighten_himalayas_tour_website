# Generated by Django 3.1.5 on 2022-03-08 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_newsletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('subject', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
            ],
        ),
    ]
