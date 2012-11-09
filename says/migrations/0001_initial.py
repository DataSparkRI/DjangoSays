# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Message'
        db.create_table('says_message', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('message_type', self.gf('django.db.models.fields.CharField')(default='notification', max_length=30)),
            ('duration_start', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('duration_end', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('says', ['Message'])


    def backwards(self, orm):
        # Deleting model 'Message'
        db.delete_table('says_message')


    models = {
        'says.message': {
            'Meta': {'object_name': 'Message'},
            'duration_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'duration_start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'message_type': ('django.db.models.fields.CharField', [], {'default': "'notification'", 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['says']