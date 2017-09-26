# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EstateGroups'
        db.create_table(u'estate_groups', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estateid', self.gf('django.db.models.fields.IntegerField')(db_column=u'EstateID')),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36L)),
        ))
        db.send_create_signal(u'grid_estates', ['EstateGroups'])

        # Adding model 'EstateManagers'
        db.create_table(u'estate_managers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estateid', self.gf('django.db.models.fields.IntegerField')(db_column=u'EstateID')),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36L)),
        ))
        db.send_create_signal(u'grid_estates', ['EstateManagers'])

        # Adding model 'EstateMap'
        db.create_table(u'estate_map', (
            ('regionid', self.gf('django.db.models.fields.CharField')(max_length=36L, primary_key=True, db_column=u'RegionID')),
            ('estateid', self.gf('django.db.models.fields.IntegerField')(db_column=u'EstateID')),
        ))
        db.send_create_signal(u'grid_estates', ['EstateMap'])

        # Adding model 'EstateSettings'
        db.create_table(u'estate_settings', (
            ('estateid', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'EstateID')),
            ('estatename', self.gf('django.db.models.fields.CharField')(max_length=64L, db_column=u'EstateName', blank=True)),
            ('abuseemailtoestateowner', self.gf('django.db.models.fields.IntegerField')(db_column=u'AbuseEmailToEstateOwner')),
            ('denyanonymous', self.gf('django.db.models.fields.IntegerField')(db_column=u'DenyAnonymous')),
            ('resethomeonteleport', self.gf('django.db.models.fields.IntegerField')(db_column=u'ResetHomeOnTeleport')),
            ('fixedsun', self.gf('django.db.models.fields.IntegerField')(db_column=u'FixedSun')),
            ('denytransacted', self.gf('django.db.models.fields.IntegerField')(db_column=u'DenyTransacted')),
            ('blockdwell', self.gf('django.db.models.fields.IntegerField')(db_column=u'BlockDwell')),
            ('denyidentified', self.gf('django.db.models.fields.IntegerField')(db_column=u'DenyIdentified')),
            ('allowvoice', self.gf('django.db.models.fields.IntegerField')(db_column=u'AllowVoice')),
            ('useglobaltime', self.gf('django.db.models.fields.IntegerField')(db_column=u'UseGlobalTime')),
            ('pricepermeter', self.gf('django.db.models.fields.IntegerField')(db_column=u'PricePerMeter')),
            ('taxfree', self.gf('django.db.models.fields.IntegerField')(db_column=u'TaxFree')),
            ('allowdirectteleport', self.gf('django.db.models.fields.IntegerField')(db_column=u'AllowDirectTeleport')),
            ('redirectgridx', self.gf('django.db.models.fields.IntegerField')(db_column=u'RedirectGridX')),
            ('redirectgridy', self.gf('django.db.models.fields.IntegerField')(db_column=u'RedirectGridY')),
            ('parentestateid', self.gf('django.db.models.fields.IntegerField')(db_column=u'ParentEstateID')),
            ('sunposition', self.gf('django.db.models.fields.FloatField')(db_column=u'SunPosition')),
            ('estateskipscripts', self.gf('django.db.models.fields.IntegerField')(db_column=u'EstateSkipScripts')),
            ('billablefactor', self.gf('django.db.models.fields.FloatField')(db_column=u'BillableFactor')),
            ('publicaccess', self.gf('django.db.models.fields.IntegerField')(db_column=u'PublicAccess')),
            ('abuseemail', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'AbuseEmail')),
            ('estateowner', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'EstateOwner')),
            ('denyminors', self.gf('django.db.models.fields.IntegerField')(db_column=u'DenyMinors')),
            ('allowlandmark', self.gf('django.db.models.fields.IntegerField')(db_column=u'AllowLandmark')),
            ('allowparcelchanges', self.gf('django.db.models.fields.IntegerField')(db_column=u'AllowParcelChanges')),
            ('allowsethome', self.gf('django.db.models.fields.IntegerField')(db_column=u'AllowSetHome')),
        ))
        db.send_create_signal(u'grid_estates', ['EstateSettings'])

        # Adding model 'EstateUsers'
        db.create_table(u'estate_users', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estateid', self.gf('django.db.models.fields.IntegerField')(db_column=u'EstateID')),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36L)),
        ))
        db.send_create_signal(u'grid_estates', ['EstateUsers'])

        # Adding model 'Estateban'
        db.create_table(u'estateban', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estateid', self.gf('django.db.models.fields.IntegerField')(db_column=u'EstateID')),
            ('banneduuid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'bannedUUID')),
            ('bannedip', self.gf('django.db.models.fields.CharField')(max_length=16L, db_column=u'bannedIp')),
            ('bannediphostmask', self.gf('django.db.models.fields.CharField')(max_length=16L, db_column=u'bannedIpHostMask')),
            ('bannednamemask', self.gf('django.db.models.fields.CharField')(max_length=64L, db_column=u'bannedNameMask', blank=True)),
        ))
        db.send_create_signal(u'grid_estates', ['Estateban'])

        # Adding model 'Migrations'
        db.create_table(u'migrations', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('version', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'grid_estates', ['Migrations'])


    def backwards(self, orm):
        # Deleting model 'EstateGroups'
        db.delete_table(u'estate_groups')

        # Deleting model 'EstateManagers'
        db.delete_table(u'estate_managers')

        # Deleting model 'EstateMap'
        db.delete_table(u'estate_map')

        # Deleting model 'EstateSettings'
        db.delete_table(u'estate_settings')

        # Deleting model 'EstateUsers'
        db.delete_table(u'estate_users')

        # Deleting model 'Estateban'
        db.delete_table(u'estateban')

        # Deleting model 'Migrations'
        db.delete_table(u'migrations')


    models = {
        u'grid_estates.estateban': {
            'Meta': {'object_name': 'Estateban', 'db_table': "u'estateban'"},
            'bannedip': ('django.db.models.fields.CharField', [], {'max_length': '16L', 'db_column': "u'bannedIp'"}),
            'bannediphostmask': ('django.db.models.fields.CharField', [], {'max_length': '16L', 'db_column': "u'bannedIpHostMask'"}),
            'bannednamemask': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'db_column': "u'bannedNameMask'", 'blank': 'True'}),
            'banneduuid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'bannedUUID'"}),
            'estateid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'EstateID'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'grid_estates.estategroups': {
            'Meta': {'object_name': 'EstateGroups', 'db_table': "u'estate_groups'"},
            'estateid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'EstateID'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36L'})
        },
        u'grid_estates.estatemanagers': {
            'Meta': {'object_name': 'EstateManagers', 'db_table': "u'estate_managers'"},
            'estateid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'EstateID'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36L'})
        },
        u'grid_estates.migrations': {
            'Meta': {'object_name': 'Migrations', 'db_table': "u'migrations'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'version': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['grid_estates']