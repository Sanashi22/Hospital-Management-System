# Generated by Django 4.2.6 on 2024-01-27 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_patient_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='doctor',
        ),
    ]
