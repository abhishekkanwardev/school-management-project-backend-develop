# Generated by Django 4.1.5 on 2023-01-23 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('progress_tracking', '0003_proggressrecord_lesson_progress_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lessonprogress',
            name='ProgressScore',
        ),
        migrations.RemoveField(
            model_name='proggressrecord',
            name='lesson_progress',
        ),
        migrations.AddField(
            model_name='lessonprogress',
            name='progress_record',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='progress_tracking.proggressrecord'),
        ),
        migrations.AddField(
            model_name='lessonprogress',
            name='progressScore',
            field=models.ManyToManyField(blank=True, to='progress_tracking.progressscore'),
        ),
    ]
