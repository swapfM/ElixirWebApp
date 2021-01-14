# Generated by Django 2.2.13 on 2021-01-13 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_student', '0003_auto_20210113_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scores',
            name='assessment_type_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user_admin.assessment_type'),
        ),
        migrations.DeleteModel(
            name='assessment_type',
        ),
    ]
