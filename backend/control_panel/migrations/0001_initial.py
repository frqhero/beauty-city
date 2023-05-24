# Generated by Django 4.2.1 on 2023-05-24 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_slot', models.CharField(choices=[('0', '10-11'), ('1', '11-12'), ('2', '12-13'), ('3', '13-14'), ('4', '14-15'), ('5', '15-16'), ('6', '16-17'), ('7', '17-18'), ('8', '18-19'), ('9', '19-20')], max_length=1)),
            ],
        ),
    ]
