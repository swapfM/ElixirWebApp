# Generated by Django 2.2.13 on 2021-02-03 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='scores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(blank=True, null=True)),
                ('user_score', models.IntegerField()),
                ('total_score', models.IntegerField(default=0)),
                ('assessment_type_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user_admin.assessment_type')),
                ('batch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.batch')),
                ('level_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.module_level')),
                ('question_content_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user_admin.question_content')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.student')),
            ],
        ),
    ]
