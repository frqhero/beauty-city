# Generated by Django 4.2.1 on 2023-05-24 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0002_client_master_procedure_salon_appointment_client_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='date',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
    ]