# Generated by Django 2.1.11 on 2019-11-20 17:28

import cratedb.fields.array
import cratedb.fields.hstore
from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.hstore
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_auto_20191118_0804'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('weather_station_id', models.CharField(max_length=12, primary_key=True)),
                ('weather_station_code', models.CharField(max_length=12)),
                ('station_name', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=2, null=True)),
                ('state', models.CharField(blank=True, max_length=2, null=True)),
                ('call', models.CharField(blank=True, max_length=6, null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('elevation', models.FloatField(null=True)),
                ('elevation_uom', models.CharField(blank=True, max_length=6, null=True)),
            ],
        )
    ]
