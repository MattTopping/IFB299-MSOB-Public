# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('car_id', models.AutoField(serialize=False, primary_key=True)),
                ('makename', models.CharField(max_length=50, blank=True)),
                ('model', models.CharField(max_length=50, blank=True)),
                ('series', models.CharField(max_length=100, blank=True)),
                ('series_year', models.IntegerField(blank=True)),
                ('price_new', models.IntegerField(blank=True)),
                ('engine_size', models.DecimalField(max_digits=3, decimal_places=1, blank=True)),
                ('fuel_system', models.CharField(max_length=100, blank=True)),
                ('tank_capacity', models.IntegerField(blank=True)),
                ('horse_power', models.IntegerField(blank=True)),
                ('seating', models.IntegerField(blank=True)),
                ('standardtransmission', models.CharField(max_length=20, blank=True)),
                ('bodytype', models.CharField(max_length=50, blank=True)),
                ('drivetype', models.CharField(blank=True, max_length=3, choices=[(b'RWD', b'RWD'), (b'FWD', b'FWD'), (b'AWD', b'AWD'), (b'4WD', b'4WD')])),
                ('wheelbase', models.IntegerField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.AutoField(serialize=False, primary_key=True)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=200)),
                ('state', models.CharField(blank=True, max_length=3, choices=[(b'QLD', b'QLD'), (b'NSW', b'NSW'), (b'SA', b'SA'), (b'TAS', b'TAS'), (b'VIC', b'VIC')])),
                ('city', models.CharField(max_length=200, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StoreGarage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('store_id', models.IntegerField(default=b'1')),
                ('car_id', models.IntegerField(default=b'1')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('email', models.EmailField(max_length=75)),
                ('password', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female'), (b'N', b'Not Specified')])),
                ('birthday', models.DateField()),
                ('address', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
