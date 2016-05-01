# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('drug', models.CharField(unique=True, max_length=40)),
                ('branch', models.CharField(unique=True, max_length=40)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
