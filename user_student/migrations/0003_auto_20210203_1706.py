# Generated by Django 2.2.13 on 2021-02-03 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_student', '0002_auto_20210203_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scores',
            name='date_time',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='scores',
            name='total_score',
            field=models.IntegerField(),
        ),
    ]
