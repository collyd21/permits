# Generated by Django 3.1.6 on 2021-06-30 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mewp', '0009_auto_20210630_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mewp',
            name='question_2',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('na', 'NA')], max_length=80),
        ),
        migrations.AlterField(
            model_name='mewp',
            name='question_3',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('na', 'NA')], max_length=80),
        ),
    ]
