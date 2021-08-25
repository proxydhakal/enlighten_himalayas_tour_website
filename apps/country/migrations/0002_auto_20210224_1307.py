# Generated by Django 3.1.5 on 2021-02-24 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destinations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slogan', models.CharField(max_length=255, unique=True)),
                ('cover_image', models.ImageField(upload_to='destination/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Country'},
        ),
    ]