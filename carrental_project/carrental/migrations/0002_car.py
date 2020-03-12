# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrental', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('makename', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('series', models.CharField(max_length=100)),
                ('series_year', models.IntegerField()),
                ('price_new', models.IntegerField()),
                ('engine_size', models.DecimalField(max_digits=3, decimal_places=1)),
                ('fuel_system', models.CharField(max_length=100)),
                ('tank_capacity', models.IntegerField()),
                ('horse_power', models.IntegerField()),
                ('seating', models.IntegerField()),
                ('standardtransmission', models.CharField(max_length=20)),
                ('bodytype', models.CharField(max_length=50)),
                ('drivetype', models.CharField(max_length=1, choices=[(b'RWD', b'RWD'), (b'FWD', b'FWD'), (b'AWD', b'AWD'), (b'4WD', b'4WD')])),
                ('wheelbase', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
