# Generated by Django 4.2.1 on 2023-05-27 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0004_procedure_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='client',
        ),
        migrations.AddField(
            model_name='appointment',
            name='phone_number',
            field=models.CharField(default='', max_length=12),
            preserve_default=False,
        ),
    ]
