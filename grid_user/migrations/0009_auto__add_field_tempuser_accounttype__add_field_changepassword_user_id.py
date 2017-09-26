# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TempUser.accounttype'
        db.add_column(u'grid_user_tempuser', 'accounttype',
                      self.gf('django.db.models.fields.CharField')(default='basic membership', max_length=64, blank=True),
                      keep_default=False)

        # Adding field 'ChangePassword.user_id'
        db.add_column(u'grid_user_changepassword', 'user_id',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'TempUser.accounttype'
        db.delete_column(u'grid_user_tempuser', 'accounttype')

        # Deleting field 'ChangePassword.user_id'
        db.delete_column(u'grid_user_changepassword', 'user_id')


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
            'password': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
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
            'accounttype': ('django.db.models.fields.CharField', [], {'default': "'basic membership'", 'max_length': '64', 'blank': 'True'}),
            'activation_key': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'avatarname': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '95'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'securtya': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'securtyq': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'grid_user.user': {
            'Meta': {'object_name': 'User'},
            'avatarname': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'dob': ('django.db.models.fields.DateField', [], {}),
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
            'securtya': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'securtyq': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user_level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['grid_user']