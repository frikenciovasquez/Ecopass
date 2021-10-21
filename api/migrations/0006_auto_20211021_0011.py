# Generated by Django 3.2.7 on 2021-10-21 00:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20211019_0013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='alquiler',
        ),
        migrations.AddField(
            model_name='service',
            name='servicios_disponibles',
            field=models.ManyToManyField(to='api.Rental'),
        ),
        migrations.AlterField(
            model_name='travel',
            name='date_end',
            field=models.DateField(default=datetime.date(2021, 10, 21), verbose_name='fecha de fin'),
        ),
        migrations.AlterField(
            model_name='travel',
            name='date_start',
            field=models.DateField(default=datetime.date(2021, 10, 21), verbose_name='fecha de inicio'),
        ),
    ]
