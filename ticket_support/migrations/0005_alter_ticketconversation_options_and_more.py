# Generated by Django 4.1.5 on 2023-02-22 10:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket_support', '0004_ticket_closed_by'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticketconversation',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='ticket',
            name='assignees',
            field=models.ManyToManyField(related_name='ticket_assgnees', to=settings.AUTH_USER_MODEL, verbose_name='assignees'),
        ),
    ]