# Generated by Django 5.0.1 on 2024-01-31 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_appointment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appointment',
        ),
    ]
