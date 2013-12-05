# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Maintainer'
        db.create_table(u'crmapp_maintainer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('phonenumber', self.gf('django.db.models.fields.IntegerField')(max_length=200)),
            ('headImg', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('remarks', self.gf('django.db.models.fields.TextField')()),
            ('identity', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, blank=True)),
        ))
        db.send_create_signal(u'crmapp', ['Maintainer'])

        # Adding model 'Business'
        db.create_table(u'crmapp_business', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('shopname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('district', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('bmap', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('adder', self.gf('django.db.models.fields.related.ForeignKey')(related_name='adder', to=orm['crmapp.Maintainer'])),
            ('addtime', self.gf('django.db.models.fields.DateField')()),
            ('condition', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('installor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='installor', to=orm['crmapp.Maintainer'])),
            ('installtime', self.gf('django.db.models.fields.DateField')()),
            ('remarks', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'crmapp', ['Business'])

        # Adding M2M table for field tag on 'Business'
        m2m_table_name = db.shorten_name(u'crmapp_business_tag')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('business', models.ForeignKey(orm[u'crmapp.business'], null=False)),
            ('tag', models.ForeignKey(orm[u'crmapp.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['business_id', 'tag_id'])

        # Adding model 'Tag'
        db.create_table(u'crmapp_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'crmapp', ['Tag'])

        # Adding model 'Routing'
        db.create_table(u'crmapp_routing', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('gateway', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('is_main', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('mac', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('ssid', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('lanip', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('port', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('remarks', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('business', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['crmapp.Business'], unique=True)),
        ))
        db.send_create_signal(u'crmapp', ['Routing'])

        # Adding model 'CooperInfo'
        db.create_table(u'crmapp_cooperinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('starttime', self.gf('django.db.models.fields.DateField')()),
            ('endtime', self.gf('django.db.models.fields.DateField')()),
            ('cooperImg', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('business', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['crmapp.Business'], unique=True)),
        ))
        db.send_create_signal(u'crmapp', ['CooperInfo'])


    def backwards(self, orm):
        # Deleting model 'Maintainer'
        db.delete_table(u'crmapp_maintainer')

        # Deleting model 'Business'
        db.delete_table(u'crmapp_business')

        # Removing M2M table for field tag on 'Business'
        db.delete_table(db.shorten_name(u'crmapp_business_tag'))

        # Deleting model 'Tag'
        db.delete_table(u'crmapp_tag')

        # Deleting model 'Routing'
        db.delete_table(u'crmapp_routing')

        # Deleting model 'CooperInfo'
        db.delete_table(u'crmapp_cooperinfo')


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
            'adder': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'adder'", 'to': u"orm['crmapp.Maintainer']"}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'addtime': ('django.db.models.fields.DateField', [], {}),
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
            'business': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['crmapp.Business']", 'unique': 'True'}),
            'gateway': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_main': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lanip': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'mac': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'port': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
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