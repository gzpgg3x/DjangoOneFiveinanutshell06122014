# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Post.owner'
        db.delete_column(u'posts_post', 'owner_id')


    def backwards(self, orm):
        # Adding field 'Post.owner'
        db.add_column(u'posts_post', 'owner',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['auth.User']),
                      keep_default=False)


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