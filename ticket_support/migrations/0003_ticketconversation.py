# Generated by Django 4.1.5 on 2023-02-22 05:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket_support', '0002_alter_ticket_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketConversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ticket_convo', to='ticket_support.ticket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ticket_convo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
