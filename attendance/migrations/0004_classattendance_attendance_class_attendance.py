# Generated by Django 4.1.5 on 2023-02-03 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_process', '0008_rename_class_progress_dismissal_class_dismissal'),
        ('attendance', '0003_rename_lesson_attendance_lesson_period'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_attendance_list', to='school_process.class')),
            ],
        ),
        migrations.AddField(
            model_name='attendance',
            name='class_attendance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attendance_list', to='attendance.classattendance'),
        ),
    ]
