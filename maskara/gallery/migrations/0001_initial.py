# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Artist'
        db.create_table('gallery_artist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('changed', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('bio', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('gallery', ['Artist'])

        # Adding model 'ArtistWork'
        db.create_table('gallery_artistwork', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('changed', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Artist'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=1024, blank=True)),
            ('material', self.gf('django.db.models.fields.CharField')(max_length=1024, blank=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True, blank=True)),
            ('theme', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('attribution', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('price', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('gallery', ['ArtistWork'])

        # Adding model 'ArtistReview'
        db.create_table('gallery_artistreview', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('changed', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=1024, blank=True)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=1024, blank=True)),
            ('translated_by', self.gf('django.db.models.fields.CharField')(max_length=1024, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('pdf', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('test', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Artist'])),
        ))
        db.send_create_signal('gallery', ['ArtistReview'])

        # Adding model 'ArtistPressRelease'
        db.create_table('gallery_artistpressrelease', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('changed', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('publisher', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('pdf', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('test', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Artist'])),
        ))
        db.send_create_signal('gallery', ['ArtistPressRelease'])

        # Adding model 'Exhibition'
        db.create_table('gallery_exhibition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('changed', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('autopublish_date', self.gf('django.db.models.fields.DateField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('gallery', ['Exhibition'])

        # Adding M2M table for field featured_artists on 'Exhibition'
        db.create_table('gallery_exhibition_featured_artists', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('exhibition', models.ForeignKey(orm['gallery.exhibition'], null=False)),
            ('artist', models.ForeignKey(orm['gallery.artist'], null=False))
        ))
        db.create_unique('gallery_exhibition_featured_artists', ['exhibition_id', 'artist_id'])

        # Adding M2M table for field featured_work on 'Exhibition'
        db.create_table('gallery_exhibition_featured_work', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('exhibition', models.ForeignKey(orm['gallery.exhibition'], null=False)),
            ('artistwork', models.ForeignKey(orm['gallery.artistwork'], null=False))
        ))
        db.create_unique('gallery_exhibition_featured_work', ['exhibition_id', 'artistwork_id'])

        # Adding model 'ExhibitionReview'
        db.create_table('gallery_exhibitionreview', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('changed', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=1024, blank=True)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=1024, blank=True)),
            ('translated_by', self.gf('django.db.models.fields.CharField')(max_length=1024, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('pdf', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('test', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('exhibition', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Exhibition'])),
        ))
        db.send_create_signal('gallery', ['ExhibitionReview'])

        # Adding model 'ExhibitionPressRelease'
        db.create_table('gallery_exhibitionpressrelease', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('changed', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('publisher', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('pdf', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('test', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('exhibition', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Exhibition'])),
        ))
        db.send_create_signal('gallery', ['ExhibitionPressRelease'])

        # Adding model 'Event'
        db.create_table('gallery_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('changed', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('time_from', self.gf('django.db.models.fields.TimeField')()),
            ('time_to', self.gf('django.db.models.fields.TimeField')()),
            ('featured_artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Artist'], null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('gallery', ['Event'])

        # Adding model 'Publication'
        db.create_table('gallery_publication', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('changed', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=1024, blank=True)),
            ('editor', self.gf('django.db.models.fields.CharField')(max_length=1024, blank=True)),
            ('publisher', self.gf('django.db.models.fields.CharField')(max_length=1024, blank=True)),
            ('isbn', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('pdf', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('available', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('gallery', ['Publication'])


    def backwards(self, orm):
        # Deleting model 'Artist'
        db.delete_table('gallery_artist')

        # Deleting model 'ArtistWork'
        db.delete_table('gallery_artistwork')

        # Deleting model 'ArtistReview'
        db.delete_table('gallery_artistreview')

        # Deleting model 'ArtistPressRelease'
        db.delete_table('gallery_artistpressrelease')

        # Deleting model 'Exhibition'
        db.delete_table('gallery_exhibition')

        # Removing M2M table for field featured_artists on 'Exhibition'
        db.delete_table('gallery_exhibition_featured_artists')

        # Removing M2M table for field featured_work on 'Exhibition'
        db.delete_table('gallery_exhibition_featured_work')

        # Deleting model 'ExhibitionReview'
        db.delete_table('gallery_exhibitionreview')

        # Deleting model 'ExhibitionPressRelease'
        db.delete_table('gallery_exhibitionpressrelease')

        # Deleting model 'Event'
        db.delete_table('gallery_event')

        # Deleting model 'Publication'
        db.delete_table('gallery_publication')


    models = {
        'gallery.artist': {
            'Meta': {'object_name': 'Artist'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'gallery.artistpressrelease': {
            'Meta': {'ordering': "['order']", 'object_name': 'ArtistPressRelease'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Artist']"}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'test': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'gallery.artistreview': {
            'Meta': {'ordering': "['order']", 'object_name': 'ArtistReview'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Artist']"}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'test': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'translated_by': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'gallery.artistwork': {
            'Meta': {'ordering': "['order']", 'object_name': 'ArtistWork'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Artist']"}),
            'attribution': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'material': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'theme': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'year': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'})
        },
        'gallery.event': {
            'Meta': {'object_name': 'Event'},
            'changed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'featured_artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Artist']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'time_from': ('django.db.models.fields.TimeField', [], {}),
            'time_to': ('django.db.models.fields.TimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        'gallery.exhibition': {
            'Meta': {'object_name': 'Exhibition'},
            'autopublish_date': ('django.db.models.fields.DateField', [], {}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'featured_artists': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['gallery.Artist']", 'null': 'True', 'blank': 'True'}),
            'featured_work': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['gallery.ArtistWork']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        'gallery.exhibitionpressrelease': {
            'Meta': {'object_name': 'ExhibitionPressRelease'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'exhibition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Exhibition']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'test': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'gallery.exhibitionreview': {
            'Meta': {'ordering': "['order']", 'object_name': 'ExhibitionReview'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'exhibition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Exhibition']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'test': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'translated_by': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'gallery.publication': {
            'Meta': {'object_name': 'Publication'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'available': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'editor': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['gallery']