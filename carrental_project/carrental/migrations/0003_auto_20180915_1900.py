# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrental', '0002_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='drivetype',
            field=models.CharField(max_length=3, choices=[(b'RWD', b'RWD'), (b'FWD', b'FWD'), (b'AWD', b'AWD'), (b'4WD', b'4WD')]),
        ),
    ]
