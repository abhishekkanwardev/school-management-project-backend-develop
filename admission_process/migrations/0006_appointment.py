# Generated by Django 4.0 on 2023-02-06 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admission_process', '0005_alter_admissionapplication_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateField(help_text='YYYY-MM-DD')),
                ('appointment_time', models.IntegerField(choices=[(0, '09:00'), (1, '10:00'), (2, '11:00'), (3, '12:00'), (4, '01:00'), (5, '02:00'), (6, '03:00'), (7, '04:00'), (8, '05:00')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admission_application', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='admission_process.admissionapplication')),
            ],
            options={
                'unique_together': {('appointment_date', 'appointment_time')},
            },
        ),
    ]