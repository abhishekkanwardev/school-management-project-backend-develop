# Generated by Django 4.1.5 on 2023-01-23 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress_tracking', '0002_progressscore_remove_proggressrecord_lesson_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='proggressrecord',
            name='lesson_progress',
            field=models.ManyToManyField(blank=True, null=True, to='progress_tracking.lessonprogress'),
        ),
        migrations.RemoveField(
            model_name='lessonprogress',
            name='ProgressScore',
        ),
        migrations.AddField(
            model_name='lessonprogress',
            name='ProgressScore',
            field=models.ManyToManyField(blank=True, null=True, to='progress_tracking.progressscore'),
        ),
    ]
