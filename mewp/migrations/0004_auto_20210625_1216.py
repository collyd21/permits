# Generated by Django 3.1.6 on 2021-06-25 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mewp', '0003_auto_20210625_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mewp',
            name='date',
            field=models.DateField(),
        ),
    ]
