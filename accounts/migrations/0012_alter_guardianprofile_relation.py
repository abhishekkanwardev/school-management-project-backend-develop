# Generated by Django 4.1.5 on 2023-01-12 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_studentprofile_class_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guardianprofile',
            name='relation',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
    ]