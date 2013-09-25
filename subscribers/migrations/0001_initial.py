# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Subscriber'
        db.create_table('subscribers_subscriber', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('changed', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('tel_no', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('cell_no', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=1024, blank=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
        ))
        db.send_create_signal('subscribers', ['Subscriber'])


    def backwards(self, orm):
        # Deleting model 'Subscriber'
        db.delete_table('subscribers_subscriber')


    models = {
        'subscribers.subscriber': {
            'Meta': {'object_name': 'Subscriber'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'cell_no': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'tel_no': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'})
        }
    }

    complete_apps = ['subscribers']