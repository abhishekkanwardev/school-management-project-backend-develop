# Generated by Django 4.1.5 on 2023-02-22 10:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket_support', '0005_alter_ticketconversation_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='assignees',
            field=models.ManyToManyField(related_name='ticket_assignees', to=settings.AUTH_USER_MODEL, verbose_name='assignees'),
        ),
    ]