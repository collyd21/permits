# Generated by Django 3.1.6 on 2021-06-30 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mewp', '0007_auto_20210628_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mewp',
            name='question_1',
            field=models.CharField(choices=[('question_1_yes', 'Yes'), ('question_1_no', 'No'), ('question_1_na', 'NA')], max_length=80),
        ),
    ]