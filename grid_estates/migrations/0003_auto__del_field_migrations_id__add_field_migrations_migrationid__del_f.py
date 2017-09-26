# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Migrations.id'
        #db.delete_column(u'migrations', u'id')

        # Adding field 'Migrations.migrationid'
        db.add_column(u'migrations', 'migrationid',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True, db_column=u'migrationid'),
                      keep_default=False)

        # Deleting field 'EstateUsers.id'
        #db.delete_column(u'estate_users', u'id')

        # Adding field 'EstateUsers.estateuserid'
        db.add_column(u'estate_users', 'estateuserid',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True, db_column=u'EstateUserID'),
                      keep_default=False)

        # Deleting field 'Estateban.id'
        #db.delete_column(u'estateban', u'id')

        # Adding field 'Estateban.estatebanid'
        db.add_column(u'estateban', 'estatebanid',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True, db_column=u'EstateBanID'),
                      keep_default=False)

        # Deleting field 'EstateManagers.id'
        #db.delete_column(u'estate_managers', u'id')

        # Adding field 'EstateManagers.estatemanagerid'
        db.add_column(u'estate_managers', 'estatemanagerid',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True, db_column=u'EstateManagerID'),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Migrations.id'
        db.add_column(u'migrations', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True),
                      keep_default=False)

        # Deleting field 'Migrations.migrationid'
        db.delete_column(u'migrations', u'migrationid')

        # Adding field 'EstateUsers.id'
        db.add_column(u'estate_users', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True),
                      keep_default=False)

        # Deleting field 'EstateUsers.estateuserid'
        db.delete_column(u'estate_users', u'EstateUserID')

        # Adding field 'Estateban.id'
        db.add_column(u'estateban', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True),
                      keep_default=False)

        # Deleting field 'Estateban.estatebanid'
        db.delete_column(u'estateban', u'EstateBanID')

        # Adding field 'EstateManagers.id'
        db.add_column(u'estate_managers', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True),
                      keep_default=False)

        # Deleting field 'EstateManagers.estatemanagerid'
        db.delete_column(u'estate_managers', u'EstateManagerID')


    models = {
        u'grid_estates.estateban': {
            'Meta': {'object_name': 'Estateban', 'db_table': "u'estateban'"},
            'bannedip': ('django.db.models.fields.CharField', [], {'max_length': '16L', 'db_column': "u'bannedIp'"}),
            'bannediphostmask': ('django.db.models.fields.CharField', [], {'max_length': '16L', 'db_column': "u'bannedIpHostMask'"}),
            'bannednamemask': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'db_column': "u'bannedNameMask'", 'blank': 'True'}),
            'banneduuid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'bannedUUID'"}),
            'estatebanid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'EstateBanID'"}),
            'estateid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'EstateID'"})
        },
        u'grid_estates.estategroups': {
            'Meta': {'object_name': 'EstateGroups', 'db_table': "u'estate_groups'"},
            'estategroupid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'EstateGroupID'"}),
            'estateid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'EstateID'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36L'})
        },
        u'grid_estates.estatemanagers': {
            'Meta': {'object_name': 'EstateManagers', 'db_table': "u'estate_managers'"},
            'estateid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'EstateID'"}),
            'estatemanagerid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'EstateManagerID'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36L'})
        },
        u'grid_estates.estatemap': {
            'Meta': {'object_name': 'EstateMap', 'db_table': "u'estate_map'"},
            'estateid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'EstateID'"}),
            'regionid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'primary_key': 'True', 'db_column': "u'RegionID'"})
        },
        u'grid_estates.estatesettings': {
            'Meta': {'object_name': 'EstateSettings', 'db_table': "u'estate_settings'"},
            'abuseemail': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'AbuseEmail'"}),
            'abuseemailtoestateowner': ('django.db.models.fields.IntegerField', [], {'db_column': "u'AbuseEmailToEstateOwner'"}),
            'allowdirectteleport': ('django.db.models.fields.IntegerField', [], {'db_column': "u'AllowDirectTeleport'"}),
            'allowlandmark': ('django.db.models.fields.IntegerField', [], {'db_column': "u'AllowLandmark'"}),
            'allowparcelchanges': ('django.db.models.fields.IntegerField', [], {'db_column': "u'AllowParcelChanges'"}),
            'allowsethome': ('django.db.models.fields.IntegerField', [], {'db_column': "u'AllowSetHome'"}),
            'allowvoice': ('django.db.models.fields.IntegerField', [], {'db_column': "u'AllowVoice'"}),
            'billablefactor': ('django.db.models.fields.FloatField', [], {'db_column': "u'BillableFactor'"}),
            'blockdwell': ('django.db.models.fields.IntegerField', [], {'db_column': "u'BlockDwell'"}),
            'denyanonymous': ('django.db.models.fields.IntegerField', [], {'db_column': "u'DenyAnonymous'"}),
            'denyidentified': ('django.db.models.fields.IntegerField', [], {'db_column': "u'DenyIdentified'"}),
            'denyminors': ('django.db.models.fields.IntegerField', [], {'db_column': "u'DenyMinors'"}),
            'denytransacted': ('django.db.models.fields.IntegerField', [], {'db_column': "u'DenyTransacted'"}),
            'estateid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'EstateID'"}),
            'estatename': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'db_column': "u'EstateName'", 'blank': 'True'}),
            'estateowner': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'EstateOwner'"}),
            'estateskipscripts': ('django.db.models.fields.IntegerField', [], {'db_column': "u'EstateSkipScripts'"}),
            'fixedsun': ('django.db.models.fields.IntegerField', [], {'db_column': "u'FixedSun'"}),
            'parentestateid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'ParentEstateID'"}),
            'pricepermeter': ('django.db.models.fields.IntegerField', [], {'db_column': "u'PricePerMeter'"}),
            'publicaccess': ('django.db.models.fields.IntegerField', [], {'db_column': "u'PublicAccess'"}),
            'redirectgridx': ('django.db.models.fields.IntegerField', [], {'db_column': "u'RedirectGridX'"}),
            'redirectgridy': ('django.db.models.fields.IntegerField', [], {'db_column': "u'RedirectGridY'"}),
            'resethomeonteleport': ('django.db.models.fields.IntegerField', [], {'db_column': "u'ResetHomeOnTeleport'"}),
            'sunposition': ('django.db.models.fields.FloatField', [], {'db_column': "u'SunPosition'"}),
            'taxfree': ('django.db.models.fields.IntegerField', [], {'db_column': "u'TaxFree'"}),
            'useglobaltime': ('django.db.models.fields.IntegerField', [], {'db_column': "u'UseGlobalTime'"})
        },
        u'grid_estates.estateusers': {
            'Meta': {'object_name': 'EstateUsers', 'db_table': "u'estate_users'"},
            'estateid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'EstateID'"}),
            'estateuserid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'EstateUserID'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36L'})
        },
        u'grid_estates.migrations': {
            'Meta': {'object_name': 'Migrations', 'db_table': "u'migrations'"},
            'migrationid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'migrationid'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'version': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['grid_estates']