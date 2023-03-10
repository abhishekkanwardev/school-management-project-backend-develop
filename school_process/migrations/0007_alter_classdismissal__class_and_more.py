# Generated by Django 4.1.5 on 2023-02-03 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_process', '0006_classdismissal_dismissal_class_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classdismissal',
            name='_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_dismissal_list', to='school_process.class'),
        ),
        migrations.AlterField(
            model_name='dismissal',
            name='class_progress',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dismissal_list', to='school_process.classdismissal'),
        ),
    ]
