# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Guest.event'
        db.add_column(u'engine_guest', 'event',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['engine.Event'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Guest.event'
        db.delete_column(u'engine_guest', 'event_id')


    models = {
        u'engine.event': {
            'Meta': {'object_name': 'Event'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'engine.guest': {
            'Meta': {'object_name': 'Guest'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['engine.Event']", 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['engine']