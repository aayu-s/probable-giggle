# Generated by Django 2.2 on 2020-12-01 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20201201_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
