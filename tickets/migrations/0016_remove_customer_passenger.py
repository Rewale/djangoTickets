# Generated by Django 3.2.7 on 2021-10-09 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0015_alter_ticket_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='passenger',
        ),
    ]