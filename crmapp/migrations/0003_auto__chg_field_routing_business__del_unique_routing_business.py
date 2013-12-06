# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Routing', fields ['business']
        db.delete_unique(u'crmapp_routing', ['business_id'])


        # Changing field 'Routing.business'
        db.alter_column(u'crmapp_routing', 'business_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crmapp.Business']))

    def backwards(self, orm):

        # Changing field 'Routing.business'
        db.alter_column(u'crmapp_routing', 'business_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['crmapp.Business'], unique=True))
        # Adding unique constraint on 'Routing', fields ['business']
        db.create_unique(u'crmapp_routing', ['business_id'])


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
        u'crmapp.business': {
            'Meta': {'ordering': "['number']", 'object_name': 'Business'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'bmap': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'condition': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'installor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'installor'", 'to': u"orm['crmapp.Maintainer']"}),
            'installtime': ('django.db.models.fields.DateField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'remarks': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'shopname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['crmapp.Tag']", 'symmetrical': 'False'})
        },
        u'crmapp.cooperinfo': {
            'Meta': {'ordering': "['number']", 'object_name': 'CooperInfo'},
            'business': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['crmapp.Business']", 'unique': 'True'}),
            'cooperImg': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'desc': ('django.db.models.fields.TextField', [], {}),
            'endtime': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'starttime': ('django.db.models.fields.DateField', [], {})
        },
        u'crmapp.maintainer': {
            'Meta': {'ordering': "['number']", 'object_name': 'Maintainer'},
            'headImg': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identity': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phonenumber': ('django.db.models.fields.IntegerField', [], {'max_length': '200'}),
            'remarks': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'blank': 'True'})
        },
        u'crmapp.routing': {
            'Meta': {'ordering': "['number']", 'object_name': 'Routing'},
            'business': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crmapp.Business']", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mac': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'remarks': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'ssid': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'crmapp.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['crmapp']