# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ArtistPressRelease.image'
        db.alter_column('gallery_artistpressrelease', 'image', self.gf('filebrowser.fields.FileBrowseField')(max_length=512, null=True))

        # Changing field 'ArtistPressRelease.pdf'
        db.alter_column('gallery_artistpressrelease', 'pdf', self.gf('filebrowser.fields.FileBrowseField')(max_length=512, null=True))

        # Changing field 'GalleryPerson.image'
        db.alter_column('gallery_galleryperson', 'image', self.gf('filebrowser.fields.FileBrowseField')(max_length=512, null=True))

        # Changing field 'EventReview.pdf'
        db.alter_column('gallery_eventreview', 'pdf', self.gf('filebrowser.fields.FileBrowseField')(max_length=512, null=True))

        # Changing field 'ExhibitionReview.pdf'
        db.alter_column('gallery_exhibitionreview', 'pdf', self.gf('filebrowser.fields.FileBrowseField')(max_length=512, null=True))

        # Changing field 'EventPressRelease.image'
        db.alter_column('gallery_eventpressrelease', 'image', self.gf('filebrowser.fields.FileBrowseField')(max_length=512, null=True))

        # Changing field 'EventPressRelease.pdf'
        db.alter_column('gallery_eventpressrelease', 'pdf', self.gf('filebrowser.fields.FileBrowseField')(max_length=512, null=True))

        # Changing field 'ArtistReview.pdf'
        db.alter_column('gallery_artistreview', 'pdf', self.gf('filebrowser.fields.FileBrowseField')(max_length=512, null=True))
        # Deleting field 'Artist.press_pdf'
        db.delete_column('gallery_artist', 'press_pdf')

        # Adding field 'Artist.pdf'
        db.add_column('gallery_artist', 'pdf',
                      self.gf('filebrowser.fields.FileBrowseField')(max_length=512, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Artist.image'
        db.alter_column('gallery_artist', 'image', self.gf('filebrowser.fields.FileBrowseField')(max_length=512, null=True))

        # Changing field 'Artist.bio_pdf'
        db.alter_column('gallery_artist', 'bio_pdf', self.gf('filebrowser.fields.FileBrowseField')(max_length=512, null=True))

        # Changing field 'ArtistNews.image'
        db.alter_column('gallery_artistnews', 'image', self.gf('filebrowser.fields.FileBrowseField')(max_length=512, null=True))

        # Changing field 'ExhibitionPressRelease.image'
        db.alter_column('gallery_exhibitionpressrelease', 'image', self.gf('filebrowser.fields.FileBrowseField')(max_length=512, null=True))

        # Changing field 'ExhibitionPressRelease.pdf'
        db.alter_column('gallery_exhibitionpressrelease', 'pdf', self.gf('filebrowser.fields.FileBrowseField')(max_length=512, null=True))

        # Changing field 'ArtistWork.image'
        db.alter_column('gallery_artistwork', 'image', self.gf('filebrowser.fields.FileBrowseField')(max_length=512, null=True))
        # Deleting field 'Exhibition.cropping'
        db.delete_column('gallery_exhibition', 'cropping')


        # Changing field 'Exhibition.image'
        db.alter_column('gallery_exhibition', 'image', self.gf('filebrowser.fields.FileBrowseField')(max_length=512, null=True))

        # Changing field 'Publication.image'
        db.alter_column('gallery_publication', 'image', self.gf('filebrowser.fields.FileBrowseField')(max_length=512, null=True))

        # Changing field 'Publication.pdf'
        db.alter_column('gallery_publication', 'pdf', self.gf('filebrowser.fields.FileBrowseField')(max_length=512, null=True))

        # Changing field 'Event.image'
        db.alter_column('gallery_event', 'image', self.gf('filebrowser.fields.FileBrowseField')(max_length=512, null=True))

    def backwards(self, orm):

        # Changing field 'ArtistPressRelease.image'
        db.alter_column('gallery_artistpressrelease', 'image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100))

        # Changing field 'ArtistPressRelease.pdf'
        db.alter_column('gallery_artistpressrelease', 'pdf', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100))

        # Changing field 'GalleryPerson.image'
        db.alter_column('gallery_galleryperson', 'image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100))

        # Changing field 'EventReview.pdf'
        db.alter_column('gallery_eventreview', 'pdf', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100))

        # Changing field 'ExhibitionReview.pdf'
        db.alter_column('gallery_exhibitionreview', 'pdf', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100))

        # Changing field 'EventPressRelease.image'
        db.alter_column('gallery_eventpressrelease', 'image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100))

        # Changing field 'EventPressRelease.pdf'
        db.alter_column('gallery_eventpressrelease', 'pdf', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100))

        # Changing field 'ArtistReview.pdf'
        db.alter_column('gallery_artistreview', 'pdf', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100))
        # Adding field 'Artist.press_pdf'
        db.add_column('gallery_artist', 'press_pdf',
                      self.gf('django.db.models.fields.files.FileField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Deleting field 'Artist.pdf'
        db.delete_column('gallery_artist', 'pdf')


        # Changing field 'Artist.image'
        db.alter_column('gallery_artist', 'image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100))

        # Changing field 'Artist.bio_pdf'
        db.alter_column('gallery_artist', 'bio_pdf', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100))

        # Changing field 'ArtistNews.image'
        db.alter_column('gallery_artistnews', 'image', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100))

        # Changing field 'ExhibitionPressRelease.image'
        db.alter_column('gallery_exhibitionpressrelease', 'image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100))

        # Changing field 'ExhibitionPressRelease.pdf'
        db.alter_column('gallery_exhibitionpressrelease', 'pdf', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100))

        # Changing field 'ArtistWork.image'
        db.alter_column('gallery_artistwork', 'image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100))
        # Adding field 'Exhibition.cropping'
        db.add_column('gallery_exhibition', 'cropping',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)


        # Changing field 'Exhibition.image'
        db.alter_column('gallery_exhibition', 'image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100))

        # Changing field 'Publication.image'
        db.alter_column('gallery_publication', 'image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100))

        # Changing field 'Publication.pdf'
        db.alter_column('gallery_publication', 'pdf', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100))

        # Changing field 'Event.image'
        db.alter_column('gallery_event', 'image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100))

    models = {
        'gallery.artist': {
            'Meta': {'ordering': "['name']", 'object_name': 'Artist'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'bio_pdf': ('filebrowser.fields.FileBrowseField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'birth_location': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'is_represented': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'pdf': ('filebrowser.fields.FileBrowseField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'gallery.artistaward': {
            'Meta': {'object_name': 'ArtistAward'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Artist']"}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {'max_length': '4'})
        },
        'gallery.artistcollection': {
            'Meta': {'object_name': 'ArtistCollection'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Artist']"}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {'max_length': '4'})
        },
        'gallery.artisteducation': {
            'Meta': {'object_name': 'ArtistEducation'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Artist']"}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {'max_length': '4'})
        },
        'gallery.artistgroupexhib': {
            'Meta': {'object_name': 'ArtistGroupExhib'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Artist']"}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {'max_length': '4'})
        },
        'gallery.artistnews': {
            'Meta': {'object_name': 'ArtistNews'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Artist']"}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'gallery.artistpress': {
            'Meta': {'object_name': 'ArtistPress'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Artist']"}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {'max_length': '4'})
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
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'pdf': ('filebrowser.fields.FileBrowseField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
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
            'pdf': ('filebrowser.fields.FileBrowseField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'test': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'translated_by': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'gallery.artistsoloexhib': {
            'Meta': {'object_name': 'ArtistSoloExhib'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Artist']"}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {'max_length': '4'})
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
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'is_selected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'material': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'size': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'size_text': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'theme': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'year': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'})
        },
        'gallery.artistworkimage': {
            'Meta': {'ordering': "['order']", 'object_name': 'ArtistWorkImage'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'is_hires': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'work': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.ArtistWork']"})
        },
        'gallery.event': {
            'Meta': {'object_name': 'Event'},
            'changed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'featured_artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Artist']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'is_front_page': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'time_from': ('django.db.models.fields.TimeField', [], {}),
            'time_to': ('django.db.models.fields.TimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        'gallery.eventpressrelease': {
            'Meta': {'object_name': 'EventPressRelease'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'pdf': ('filebrowser.fields.FileBrowseField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'gallery.eventreview': {
            'Meta': {'ordering': "['order']", 'object_name': 'EventReview'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'pdf': ('filebrowser.fields.FileBrowseField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'translated_by': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'gallery.exhibition': {
            'Meta': {'object_name': 'Exhibition'},
            'autopublish_date': ('django.db.models.fields.DateField', [], {}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'curated_by': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'featured_artists': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['gallery.Artist']", 'null': 'True', 'blank': 'True'}),
            'featured_work': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['gallery.ArtistWork']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'is_front_page': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'preview_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'preview_end_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'preview_start_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
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
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'pdf': ('filebrowser.fields.FileBrowseField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
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
            'pdf': ('filebrowser.fields.FileBrowseField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'translated_by': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'gallery.galleryperson': {
            'Meta': {'object_name': 'GalleryPerson'},
            'changed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'gallery.publication': {
            'Meta': {'object_name': 'Publication'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Artist']", 'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'available': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'editor': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Event']", 'null': 'True', 'blank': 'True'}),
            'exhibition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Exhibition']", 'null': 'True', 'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'pdf': ('filebrowser.fields.FileBrowseField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['gallery']