# Generated by Django 4.0 on 2023-01-19 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_process', '0003_dismissal'),
    ]

    operations = [
        migrations.AddField(
            model_name='dismissal',
            name='status',
            field=models.CharField(choices=[('Waiting', 'Waiting'), ('Approved', 'Approved'), ('Reject', 'Reject')], default='Waiting', max_length=10),
        ),
        migrations.AlterField(
            model_name='dismissal',
            name='dismissal_type',
            field=models.CharField(choices=[('Regular', 'Regular'), ('Early', 'Early')], default='Regular', max_length=10),
        ),
    ]
