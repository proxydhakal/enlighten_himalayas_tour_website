# Generated by Django 3.1.5 on 2021-02-24 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210217_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='package_name',
            field=models.CharField(blank=True, choices=[('0', 'Everest'), ('1', 'Annapurna'), ('2', 'Langtang'), ('3', 'Dolpo')], max_length=2, null=True),
        ),
    ]
