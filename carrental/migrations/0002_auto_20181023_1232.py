# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrental', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storegarage',
            name='car_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='storegarage',
            name='store_id',
            field=models.IntegerField(),
        ),
    ]
