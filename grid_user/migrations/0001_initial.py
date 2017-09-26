# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'grid_user_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=255, db_index=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('principal_id', self.gf('django.db.models.fields.CharField')(max_length=36)),
            ('scope_id', self.gf('django.db.models.fields.CharField')(default='00000000-0000-0000-0000-000000000000', max_length=36)),
            ('user_level', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_admin', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'grid_user', ['User'])

        # Adding model 'TempUser'
        db.create_table(u'grid_user_tempuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=95)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('activation_key', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'grid_user', ['TempUser'])

        # Adding model 'ChangeEmail'
        db.create_table(u'grid_user_changeemail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=95)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('activation_key', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'grid_user', ['ChangeEmail'])

        # Adding model 'ChangePassword'
        db.create_table(u'grid_user_changepassword', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('activation_key', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'grid_user', ['ChangePassword'])

        # Adding model 'SyncUser'
        db.create_table(u'grid_user_syncuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=255, db_index=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('principal_id', self.gf('django.db.models.fields.CharField')(max_length=36)),
            ('scope_id', self.gf('django.db.models.fields.CharField')(default='00000000-0000-0000-0000-000000000000', max_length=36)),
            ('user_level', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'grid_user', ['SyncUser'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'grid_user_user')

        # Deleting model 'TempUser'
        db.delete_table(u'grid_user_tempuser')

        # Deleting model 'ChangeEmail'
        db.delete_table(u'grid_user_changeemail')

        # Deleting model 'ChangePassword'
        db.delete_table(u'grid_user_changepassword')

        # Deleting model 'SyncUser'
        db.delete_table(u'grid_user_syncuser')


    models = {
        u'grid_user.changeemail': {
            'Meta': {'object_name': 'ChangeEmail'},
            'activation_key': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '95'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'grid_user.changepassword': {
            'Meta': {'object_name': 'ChangePassword'},
            'activation_key': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'grid_user.syncuser': {
            'Meta': {'object_name': 'SyncUser'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'principal_id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'scope_id': ('django.db.models.fields.CharField', [], {'default': "'00000000-0000-0000-0000-000000000000'", 'max_length': '36'}),
            'user_level': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'grid_user.tempuser': {
            'Meta': {'object_name': 'TempUser'},
            'activation_key': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '95'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'grid_user.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'principal_id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'scope_id': ('django.db.models.fields.CharField', [], {'default': "'00000000-0000-0000-0000-000000000000'", 'max_length': '36'}),
            'user_level': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['grid_user']