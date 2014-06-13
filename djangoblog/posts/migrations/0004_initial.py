# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table(u'posts_post', (
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('machine_name', self.gf('django.db.models.fields.SlugField')(max_length=255, primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('publication_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'posts', ['Post'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table(u'posts_post')


    models = {
        u'posts.post': {
            'Meta': {'ordering': "[u'-publication_date']", 'object_name': 'Post'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'machine_name': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'primary_key': 'True'}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['posts']