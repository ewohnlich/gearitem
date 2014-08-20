# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GearItem'
        db.create_table(u'gearitem_gearitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('nameDescription', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('zone', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('agility', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('crit', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('haste', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mastery', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('multistrike', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('versatility', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ilvl', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('icon', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('slot', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('socket1', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('socket2', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('socket3', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('socket_bonus', self.gf('django.db.models.fields.CharField')(max_length=80)),
        ))
        db.send_create_signal(u'gearitem', ['GearItem'])


    def backwards(self, orm):
        # Deleting model 'GearItem'
        db.delete_table(u'gearitem_gearitem')


    models = {
        u'gearitem.gearitem': {
            'Meta': {'object_name': 'GearItem'},
            'agility': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'crit': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'haste': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ilvl': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mastery': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'multistrike': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'nameDescription': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'slot': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'socket1': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'socket2': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'socket3': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'socket_bonus': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'versatility': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'zone': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['gearitem']