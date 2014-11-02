# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gearitem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gearcontext',
            name='ilvl',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gearcontext',
            name='warforged_ilvl',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
