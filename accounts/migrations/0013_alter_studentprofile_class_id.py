# Generated by Django 4.1.5 on 2023-01-12 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_process', '0001_initial'),
        ('accounts', '0012_alter_guardianprofile_relation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='class_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school_process.class'),
        ),
    ]
