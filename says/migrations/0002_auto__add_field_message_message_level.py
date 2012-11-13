# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Message.message_level'
        db.add_column('says_message', 'message_level',
                      self.gf('django.db.models.fields.CharField')(default='info', max_length=30),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Message.message_level'
        db.delete_column('says_message', 'message_level')


    models = {
        'says.message': {
            'Meta': {'object_name': 'Message'},
            'duration_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'duration_start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'message_level': ('django.db.models.fields.CharField', [], {'default': "'info'", 'max_length': '30'}),
            'message_type': ('django.db.models.fields.CharField', [], {'default': "'notification'", 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['says']