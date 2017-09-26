# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'User.securtyq'
        db.add_column(u'grid_user_user', 'securtyq',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=255),
                      keep_default=False)

        # Adding field 'User.securtya'
        db.add_column(u'grid_user_user', 'securtya',
                      self.gf('django.db.models.fields.CharField')(default='Saudi Arabia', max_length=255),
                      keep_default=False)

        # Adding unique constraint on 'User', fields ['username']
        db.create_unique(u'grid_user_user', ['username'])


        # Changing field 'User.dob'
        db.alter_column(u'grid_user_user', 'dob', self.gf('django.db.models.fields.DateField')(default='2014-08-18'))
        # Adding field 'TempUser.username'
        db.add_column(u'grid_user_tempuser', 'username',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'TempUser.dob'
        db.add_column(u'grid_user_tempuser', 'dob',
                      self.gf('django.db.models.fields.DateField')(default='2014-08-18'),
                      keep_default=False)

        # Adding field 'TempUser.securtyq'
        db.add_column(u'grid_user_tempuser', 'securtyq',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=255),
                      keep_default=False)

        # Adding field 'TempUser.securtya'
        db.add_column(u'grid_user_tempuser', 'securtya',
                      self.gf('django.db.models.fields.CharField')(default='Saudi Arabia', max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Removing unique constraint on 'User', fields ['username']
        db.delete_unique(u'grid_user_user', ['username'])

        # Deleting field 'User.securtyq'
        db.delete_column(u'grid_user_user', 'securtyq')

        # Deleting field 'User.securtya'
        db.delete_column(u'grid_user_user', 'securtya')


        # Changing field 'User.dob'
        db.alter_column(u'grid_user_user', 'dob', self.gf('django.db.models.fields.DateField')(null=True))
        # Deleting field 'TempUser.username'
        db.delete_column(u'grid_user_tempuser', 'username')

        # Deleting field 'TempUser.dob'
        db.delete_column(u'grid_user_tempuser', 'dob')

        # Deleting field 'TempUser.securtyq'
        db.delete_column(u'grid_user_tempuser', 'securtyq')

        # Deleting field 'TempUser.securtya'
        db.delete_column(u'grid_user_tempuser', 'securtya')


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
            'dob': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '95'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'securtya': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'securtyq': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'grid_user.user': {
            'Meta': {'object_name': 'User'},
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