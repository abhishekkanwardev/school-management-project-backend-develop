# Generated by Django 4.1.5 on 2023-02-03 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_process', '0005_merge_20230203_1848'),
        ('progress_tracking', '0007_remove_lessonprogress_progress_record_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_progress_list', to='school_process.class')),
            ],
        ),
        migrations.AddField(
            model_name='proggressrecord',
            name='class_progress',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='progress_record_list', to='progress_tracking.classprogress'),
        ),
    ]