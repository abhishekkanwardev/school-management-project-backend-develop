# Generated by Django 4.1.5 on 2023-02-12 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('progress_tracking', '0009_merge_20230204_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proggressrecord',
            name='class_progress',
        ),
        migrations.DeleteModel(
            name='ClassProgress',
        ),
    ]