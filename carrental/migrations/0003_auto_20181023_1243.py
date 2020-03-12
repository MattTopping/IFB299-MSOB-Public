# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrental', '0002_auto_20181023_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storegarage',
            name='car_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='storegarage',
            name='store_id',
            field=models.IntegerField(null=True),
        ),
    ]
