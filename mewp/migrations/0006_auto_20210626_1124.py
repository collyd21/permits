# Generated by Django 3.1.6 on 2021-06-26 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mewp', '0005_auto_20210626_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mewp',
            name='question_1',
            field=models.BooleanField(choices=[('question_1_yes', 'Yes'), ('question_1_no', 'No'), ('question_1_na', 'N/A')]),
        ),
    ]
