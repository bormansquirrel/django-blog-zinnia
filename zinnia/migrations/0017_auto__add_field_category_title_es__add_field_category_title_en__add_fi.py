# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Category.title_es'
        db.add_column(u'zinnia_category', 'title_es',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Category.title_en'
        db.add_column(u'zinnia_category', 'title_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Category.title_fr'
        db.add_column(u'zinnia_category', 'title_fr',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Category.title_de'
        db.add_column(u'zinnia_category', 'title_de',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Category.title_ru'
        db.add_column(u'zinnia_category', 'title_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Category.description_es'
        db.add_column(u'zinnia_category', 'description_es',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Category.description_en'
        db.add_column(u'zinnia_category', 'description_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Category.description_fr'
        db.add_column(u'zinnia_category', 'description_fr',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Category.description_de'
        db.add_column(u'zinnia_category', 'description_de',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Category.description_ru'
        db.add_column(u'zinnia_category', 'description_ru',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Entry.title_es'
        db.add_column(u'zinnia_entry', 'title_es',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Entry.title_en'
        db.add_column(u'zinnia_entry', 'title_en',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Entry.title_fr'
        db.add_column(u'zinnia_entry', 'title_fr',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Entry.title_de'
        db.add_column(u'zinnia_entry', 'title_de',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Entry.title_ru'
        db.add_column(u'zinnia_entry', 'title_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Entry.content_es'
        db.add_column(u'zinnia_entry', 'content_es',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Entry.content_en'
        db.add_column(u'zinnia_entry', 'content_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Entry.content_fr'
        db.add_column(u'zinnia_entry', 'content_fr',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Entry.content_de'
        db.add_column(u'zinnia_entry', 'content_de',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Entry.content_ru'
        db.add_column(u'zinnia_entry', 'content_ru',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Entry.excerpt_es'
        db.add_column(u'zinnia_entry', 'excerpt_es',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Entry.excerpt_en'
        db.add_column(u'zinnia_entry', 'excerpt_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Entry.excerpt_fr'
        db.add_column(u'zinnia_entry', 'excerpt_fr',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Entry.excerpt_de'
        db.add_column(u'zinnia_entry', 'excerpt_de',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Entry.excerpt_ru'
        db.add_column(u'zinnia_entry', 'excerpt_ru',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Category.title_es'
        db.delete_column(u'zinnia_category', 'title_es')

        # Deleting field 'Category.title_en'
        db.delete_column(u'zinnia_category', 'title_en')

        # Deleting field 'Category.title_fr'
        db.delete_column(u'zinnia_category', 'title_fr')

        # Deleting field 'Category.title_de'
        db.delete_column(u'zinnia_category', 'title_de')

        # Deleting field 'Category.title_ru'
        db.delete_column(u'zinnia_category', 'title_ru')

        # Deleting field 'Category.description_es'
        db.delete_column(u'zinnia_category', 'description_es')

        # Deleting field 'Category.description_en'
        db.delete_column(u'zinnia_category', 'description_en')

        # Deleting field 'Category.description_fr'
        db.delete_column(u'zinnia_category', 'description_fr')

        # Deleting field 'Category.description_de'
        db.delete_column(u'zinnia_category', 'description_de')

        # Deleting field 'Category.description_ru'
        db.delete_column(u'zinnia_category', 'description_ru')

        # Deleting field 'Entry.title_es'
        db.delete_column(u'zinnia_entry', 'title_es')

        # Deleting field 'Entry.title_en'
        db.delete_column(u'zinnia_entry', 'title_en')

        # Deleting field 'Entry.title_fr'
        db.delete_column(u'zinnia_entry', 'title_fr')

        # Deleting field 'Entry.title_de'
        db.delete_column(u'zinnia_entry', 'title_de')

        # Deleting field 'Entry.title_ru'
        db.delete_column(u'zinnia_entry', 'title_ru')

        # Deleting field 'Entry.content_es'
        db.delete_column(u'zinnia_entry', 'content_es')

        # Deleting field 'Entry.content_en'
        db.delete_column(u'zinnia_entry', 'content_en')

        # Deleting field 'Entry.content_fr'
        db.delete_column(u'zinnia_entry', 'content_fr')

        # Deleting field 'Entry.content_de'
        db.delete_column(u'zinnia_entry', 'content_de')

        # Deleting field 'Entry.content_ru'
        db.delete_column(u'zinnia_entry', 'content_ru')

        # Deleting field 'Entry.excerpt_es'
        db.delete_column(u'zinnia_entry', 'excerpt_es')

        # Deleting field 'Entry.excerpt_en'
        db.delete_column(u'zinnia_entry', 'excerpt_en')

        # Deleting field 'Entry.excerpt_fr'
        db.delete_column(u'zinnia_entry', 'excerpt_fr')

        # Deleting field 'Entry.excerpt_de'
        db.delete_column(u'zinnia_entry', 'excerpt_de')

        # Deleting field 'Entry.excerpt_ru'
        db.delete_column(u'zinnia_entry', 'excerpt_ru')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'zinnia.category': {
            'Meta': {'ordering': "['title']", 'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['zinnia.Category']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_de': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_es': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_fr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'zinnia.entry': {
            'Meta': {'ordering': "['-creation_date']", 'object_name': 'Entry'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'entries'", 'blank': 'True', 'to': u"orm['auth.User']"}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'entries'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['zinnia.Category']"}),
            'comment_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'comment_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'content_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'content_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'content_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'content_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'content_template': ('django.db.models.fields.CharField', [], {'default': "'zinnia/_entry_detail.html'", 'max_length': '250'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'detail_template': ('django.db.models.fields.CharField', [], {'default': "'entry_detail.html'", 'max_length': '250'}),
            'end_publication': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'excerpt': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'excerpt_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'excerpt_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'excerpt_es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'excerpt_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'excerpt_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'pingback_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pingback_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'related': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'related_rel_+'", 'null': 'True', 'to': "orm['zinnia.Entry']"}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'entries'", 'symmetrical': 'False', 'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'start_publication': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_de': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_es': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_fr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'trackback_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'trackback_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['zinnia']