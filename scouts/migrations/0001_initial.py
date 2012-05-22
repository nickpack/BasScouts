# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FAQEntry'
        db.create_table('scouts_faqentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('answer', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('scouts', ['FAQEntry'])

        # Adding model 'ScoutPack'
        db.create_table('scouts_scoutpack', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('uniform', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('promise', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('scouts', ['ScoutPack'])

        # Adding model 'ScoutLeader'
        db.create_table('scouts_scoutleader', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('avatar', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('scouts', ['ScoutLeader'])

        # Adding M2M table for field group on 'ScoutLeader'
        db.create_table('scouts_scoutleader_group', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scoutleader', models.ForeignKey(orm['scouts.scoutleader'], null=False)),
            ('scoutpack', models.ForeignKey(orm['scouts.scoutpack'], null=False))
        ))
        db.create_unique('scouts_scoutleader_group', ['scoutleader_id', 'scoutpack_id'])

        # Adding model 'NewsCategory'
        db.create_table('scouts_newscategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('scouts', ['NewsCategory'])

        # Adding model 'NewsArticle'
        db.create_table('scouts_newsarticle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('article_date', self.gf('django.db.models.fields.DateField')()),
            ('article_body', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('scouts', ['NewsArticle'])

        # Adding M2M table for field category on 'NewsArticle'
        db.create_table('scouts_newsarticle_category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('newsarticle', models.ForeignKey(orm['scouts.newsarticle'], null=False)),
            ('newscategory', models.ForeignKey(orm['scouts.newscategory'], null=False))
        ))
        db.create_unique('scouts_newsarticle_category', ['newsarticle_id', 'newscategory_id'])

        # Adding M2M table for field group on 'NewsArticle'
        db.create_table('scouts_newsarticle_group', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('newsarticle', models.ForeignKey(orm['scouts.newsarticle'], null=False)),
            ('scoutpack', models.ForeignKey(orm['scouts.scoutpack'], null=False))
        ))
        db.create_unique('scouts_newsarticle_group', ['newsarticle_id', 'scoutpack_id'])

        # Adding model 'Gallery'
        db.create_table('scouts_gallery', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('scouts', ['Gallery'])

        # Adding model 'GalleryImage'
        db.create_table('scouts_galleryimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('gallery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scouts.Gallery'])),
        ))
        db.send_create_signal('scouts', ['GalleryImage'])

        # Adding M2M table for field group on 'GalleryImage'
        db.create_table('scouts_galleryimage_group', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('galleryimage', models.ForeignKey(orm['scouts.galleryimage'], null=False)),
            ('scoutpack', models.ForeignKey(orm['scouts.scoutpack'], null=False))
        ))
        db.create_unique('scouts_galleryimage_group', ['galleryimage_id', 'scoutpack_id'])

    def backwards(self, orm):
        # Deleting model 'FAQEntry'
        db.delete_table('scouts_faqentry')

        # Deleting model 'ScoutPack'
        db.delete_table('scouts_scoutpack')

        # Deleting model 'ScoutLeader'
        db.delete_table('scouts_scoutleader')

        # Removing M2M table for field group on 'ScoutLeader'
        db.delete_table('scouts_scoutleader_group')

        # Deleting model 'NewsCategory'
        db.delete_table('scouts_newscategory')

        # Deleting model 'NewsArticle'
        db.delete_table('scouts_newsarticle')

        # Removing M2M table for field category on 'NewsArticle'
        db.delete_table('scouts_newsarticle_category')

        # Removing M2M table for field group on 'NewsArticle'
        db.delete_table('scouts_newsarticle_group')

        # Deleting model 'Gallery'
        db.delete_table('scouts_gallery')

        # Deleting model 'GalleryImage'
        db.delete_table('scouts_galleryimage')

        # Removing M2M table for field group on 'GalleryImage'
        db.delete_table('scouts_galleryimage_group')

    models = {
        'scouts.faqentry': {
            'Meta': {'object_name': 'FAQEntry'},
            'answer': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'scouts.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'scouts.galleryimage': {
            'Meta': {'object_name': 'GalleryImage'},
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scouts.Gallery']"}),
            'group': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scouts.ScoutPack']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'scouts.newsarticle': {
            'Meta': {'object_name': 'NewsArticle'},
            'article_body': ('django.db.models.fields.TextField', [], {}),
            'article_date': ('django.db.models.fields.DateField', [], {}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scouts.NewsCategory']", 'symmetrical': 'False'}),
            'group': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scouts.ScoutPack']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'scouts.newscategory': {
            'Meta': {'object_name': 'NewsCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'scouts.scoutleader': {
            'Meta': {'object_name': 'ScoutLeader'},
            'avatar': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'group': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['scouts.ScoutPack']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'scouts.scoutpack': {
            'Meta': {'object_name': 'ScoutPack'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'promise': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uniform': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['scouts']