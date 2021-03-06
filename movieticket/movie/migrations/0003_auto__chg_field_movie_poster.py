# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Movie.poster'
        db.alter_column(u'movie_movie', 'poster', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

    def backwards(self, orm):

        # Changing field 'Movie.poster'
        db.alter_column(u'movie_movie', 'poster', self.gf('django.db.models.fields.TextField')())

    models = {
        u'movie.actor': {
            'Meta': {'object_name': 'Actor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'movie.company': {
            'Meta': {'object_name': 'Company'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'movie.director': {
            'Meta': {'object_name': 'Director'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'movie.genre': {
            'Meta': {'object_name': 'Genre'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'movie.movie': {
            'MPAA': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movie.MPAA']"}),
            'Meta': {'object_name': 'Movie'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movie.Company']"}),
            'genre': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['movie.Genre']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'poster': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'trailer': ('django.db.models.fields.TextField', [], {})
        },
        u'movie.mpaa': {
            'Meta': {'object_name': 'MPAA'},
            'explanation': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meaning': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'movie.presentation': {
            'Meta': {'object_name': 'Presentation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'movie.presentationmovie': {
            'Meta': {'object_name': 'PresentationMovie'},
            'begin_date': ('django.db.models.fields.DateField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movie.Movie']"}),
            'presentation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movie.Presentation']"})
        }
    }

    complete_apps = ['movie']