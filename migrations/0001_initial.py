# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GearContext',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('context', models.CharField(max_length=80)),
                ('agility', models.IntegerField(default=0, blank=True)),
                ('crit', models.IntegerField(default=0, blank=True)),
                ('haste', models.IntegerField(default=0, blank=True)),
                ('mastery', models.IntegerField(default=0, blank=True)),
                ('multistrike', models.IntegerField(default=0, blank=True)),
                ('versatility', models.IntegerField(default=0, blank=True)),
                ('weapon_min', models.FloatField(default=0)),
                ('weapon_max', models.FloatField(default=0)),
                ('weapon_speed', models.FloatField(default=0)),
                ('warforged_agility', models.IntegerField(default=0, blank=True)),
                ('warforged_crit', models.IntegerField(default=0, blank=True)),
                ('warforged_haste', models.IntegerField(default=0, blank=True)),
                ('warforged_mastery', models.IntegerField(default=0, blank=True)),
                ('warforged_multistrike', models.IntegerField(default=0, blank=True)),
                ('warforged_versatility', models.IntegerField(default=0, blank=True)),
                ('warforged_weapon_min', models.FloatField(default=0)),
                ('warforged_weapon_max', models.FloatField(default=0)),
                ('warforged_weapon_speed', models.FloatField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GearItem',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('nameDescription', models.CharField(max_length=80, blank=True)),
                ('zone', models.CharField(max_length=80)),
                ('source', models.CharField(max_length=80)),
                ('agility', models.IntegerField(default=0)),
                ('crit', models.IntegerField(default=0)),
                ('haste', models.IntegerField(default=0)),
                ('mastery', models.IntegerField(default=0)),
                ('multistrike', models.IntegerField(default=0)),
                ('versatility', models.IntegerField(default=0)),
                ('weapon_min', models.FloatField(default=0)),
                ('weapon_max', models.FloatField(default=0)),
                ('weapon_speed', models.FloatField(default=0)),
                ('ilvl', models.IntegerField(default=0)),
                ('icon', models.CharField(default=b'inv_misc_questionmark', max_length=80)),
                ('slot', models.IntegerField(default=0, choices=[(15, b'Weapon'), (1, b'Head'), (2, b'Neck'), (3, b'Shoulder'), (16, b'Cloak'), (5, b'Chest'), (6, b'Waist'), (7, b'Legs'), (8, b'Feet'), (9, b'Wrist'), (10, b'Hands'), (11, b'Finger'), (12, b'Trinket'), (20, b'Chest (gown)')])),
                ('quality', models.IntegerField(default=0, choices=[(3, b'Superior'), (4, b'Epic'), (5, b'Legendary')])),
                ('socket1', models.CharField(blank=True, max_length=20, choices=[(b'red', b'Red'), (b'yellow', b'Yellow'), (b'blue', b'Blue'), (b'meta', b'Meta'), (b'chromatic', b'Chromatic'), (b'none', b'(No socket)')])),
                ('socket2', models.CharField(blank=True, max_length=20, choices=[(b'red', b'Red'), (b'yellow', b'Yellow'), (b'blue', b'Blue'), (b'meta', b'Meta'), (b'chromatic', b'Chromatic'), (b'none', b'(No socket)')])),
                ('socket3', models.CharField(blank=True, max_length=20, choices=[(b'red', b'Red'), (b'yellow', b'Yellow'), (b'blue', b'Blue'), (b'meta', b'Meta'), (b'chromatic', b'Chromatic'), (b'none', b'(No socket)')])),
                ('socket_bonus', models.CharField(max_length=80, blank=True)),
            ],
            options={
                'ordering': ['-ilvl', 'name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gem',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('agility', models.IntegerField(default=0, blank=True)),
                ('crit', models.IntegerField(default=0, blank=True)),
                ('haste', models.IntegerField(default=0, blank=True)),
                ('mastery', models.IntegerField(default=0, blank=True)),
                ('multistrike', models.IntegerField(default=0, blank=True)),
                ('versatility', models.IntegerField(default=0, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='gearcontext',
            name='gearitem',
            field=models.ForeignKey(to='gearitem.GearItem'),
            preserve_default=True,
        ),
    ]
