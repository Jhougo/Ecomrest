# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('peo_vio_count', models.CharField(max_length=255)),
                ('people_id', models.CharField(primary_key=True, serialize=False, max_length=50)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('peo_vio_date', models.CharField(max_length=255)),
                ('peo_vio_time', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicale',
            fields=[
                ('ve_vio_count', models.CharField(max_length=255)),
                ('plate', models.CharField(primary_key=True, serialize=False, max_length=20)),
                ('vio_date', models.CharField(max_length=20)),
                ('vio_time', models.CharField(max_length=20)),
                ('vehicale_type', models.CharField(max_length=20)),
                ('owner', models.CharField(max_length=20)),
                ('vehicale_brand', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=10)),
                ('type_detail', models.CharField(max_length=50)),
            ],
        ),
    ]
