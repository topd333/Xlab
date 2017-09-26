# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Avatars'
        db.create_table(u'Avatars', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('principalid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'PrincipalID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32L, db_column=u'Name')),
            ('value', self.gf('django.db.models.fields.TextField')(db_column=u'Value', blank=True)),
        ))
        db.send_create_signal(u'grid_core', ['Avatars'])

        # Adding model 'Friends'
        db.create_table(u'Friends', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('principalid', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'PrincipalID')),
            ('friend', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'Friend')),
            ('flags', self.gf('django.db.models.fields.CharField')(max_length=16L, db_column=u'Flags')),
            ('offered', self.gf('django.db.models.fields.CharField')(max_length=32L, db_column=u'Offered')),
        ))
        db.send_create_signal(u'grid_core', ['Friends'])

        # Adding model 'Griduser'
        db.create_table(u'GridUser', (
            ('userid', self.gf('django.db.models.fields.CharField')(max_length=255L, primary_key=True, db_column=u'UserID')),
            ('homeregionid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'HomeRegionID')),
            ('homeposition', self.gf('django.db.models.fields.CharField')(max_length=64L, db_column=u'HomePosition')),
            ('homelookat', self.gf('django.db.models.fields.CharField')(max_length=64L, db_column=u'HomeLookAt')),
            ('lastregionid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'LastRegionID')),
            ('lastposition', self.gf('django.db.models.fields.CharField')(max_length=64L, db_column=u'LastPosition')),
            ('lastlookat', self.gf('django.db.models.fields.CharField')(max_length=64L, db_column=u'LastLookAt')),
            ('online', self.gf('django.db.models.fields.CharField')(max_length=5L, db_column=u'Online')),
            ('login', self.gf('django.db.models.fields.CharField')(max_length=16L, db_column=u'Login')),
            ('logout', self.gf('django.db.models.fields.CharField')(max_length=16L, db_column=u'Logout')),
        ))
        db.send_create_signal(u'grid_core', ['Griduser'])

        # Adding model 'Presence'
        db.create_table(u'Presence', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('userid', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'UserID')),
            ('regionid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'RegionID')),
            ('sessionid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=36L, db_column=u'SessionID')),
            ('securesessionid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'SecureSessionID')),
            ('lastseen', self.gf('django.db.models.fields.DateTimeField')(db_column=u'LastSeen')),
        ))
        db.send_create_signal(u'grid_core', ['Presence'])

        # Adding model 'Useraccounts'
        db.create_table(u'UserAccounts', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('principalid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=36L, db_column=u'PrincipalID')),
            ('scopeid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'ScopeID')),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=64L, db_column=u'FirstName')),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=64L, db_column=u'LastName')),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=64L, db_column=u'Email', blank=True)),
            ('serviceurls', self.gf('django.db.models.fields.TextField')(db_column=u'ServiceURLs', blank=True)),
            ('created', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Created', blank=True)),
            ('userlevel', self.gf('django.db.models.fields.IntegerField')(db_column=u'UserLevel')),
            ('userflags', self.gf('django.db.models.fields.IntegerField')(db_column=u'UserFlags')),
            ('usertitle', self.gf('django.db.models.fields.CharField')(max_length=64L, db_column=u'UserTitle')),
        ))
        db.send_create_signal(u'grid_core', ['Useraccounts'])

        # Adding model 'Auth'
        db.create_table(u'auth', (
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36L, primary_key=True, db_column=u'UUID')),
            ('passwordhash', self.gf('django.db.models.fields.CharField')(max_length=32L, db_column=u'passwordHash')),
            ('passwordsalt', self.gf('django.db.models.fields.CharField')(max_length=32L, db_column=u'passwordSalt')),
            ('webloginkey', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'webLoginKey')),
            ('accounttype', self.gf('django.db.models.fields.CharField')(max_length=32L, db_column=u'accountType')),
        ))
        db.send_create_signal(u'grid_core', ['Auth'])

        # Adding model 'HgTravelingData'
        db.create_table(u'hg_traveling_data', (
            ('sessionid', self.gf('django.db.models.fields.CharField')(max_length=36L, primary_key=True, db_column=u'SessionID')),
            ('userid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'UserID')),
            ('gridexternalname', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'GridExternalName')),
            ('servicetoken', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'ServiceToken')),
            ('clientipaddress', self.gf('django.db.models.fields.CharField')(max_length=16L, db_column=u'ClientIPAddress')),
            ('myipaddress', self.gf('django.db.models.fields.CharField')(max_length=16L, db_column=u'MyIPAddress')),
            ('tmstamp', self.gf('django.db.models.fields.DateTimeField')(db_column=u'TMStamp')),
        ))
        db.send_create_signal(u'grid_core', ['HgTravelingData'])

        # Adding model 'ImOffline'
        db.create_table(u'im_offline', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'ID')),
            ('principalid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'PrincipalID')),
            ('message', self.gf('django.db.models.fields.TextField')(db_column=u'Message')),
            ('tmstamp', self.gf('django.db.models.fields.DateTimeField')(db_column=u'TMStamp')),
        ))
        db.send_create_signal(u'grid_core', ['ImOffline'])

        # Adding model 'Inventoryfolders'
        db.create_table(u'inventoryfolders', (
            ('foldername', self.gf('django.db.models.fields.CharField')(max_length=64L, db_column=u'folderName', blank=True)),
            ('type', self.gf('django.db.models.fields.IntegerField')()),
            ('version', self.gf('django.db.models.fields.IntegerField')()),
            ('folderid', self.gf('django.db.models.fields.CharField')(max_length=36L, primary_key=True, db_column=u'folderID')),
            ('agentid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'agentID', blank=True)),
            ('parentfolderid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'parentFolderID', blank=True)),
        ))
        db.send_create_signal(u'grid_core', ['Inventoryfolders'])

        # Adding model 'Inventoryitems'
        db.create_table(u'inventoryitems', (
            ('assetid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'assetID', blank=True)),
            ('assettype', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'assetType', blank=True)),
            ('inventoryname', self.gf('django.db.models.fields.CharField')(max_length=64L, db_column=u'inventoryName', blank=True)),
            ('inventorydescription', self.gf('django.db.models.fields.CharField')(max_length=128L, db_column=u'inventoryDescription', blank=True)),
            ('inventorynextpermissions', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'inventoryNextPermissions', blank=True)),
            ('inventorycurrentpermissions', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'inventoryCurrentPermissions', blank=True)),
            ('invtype', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'invType', blank=True)),
            ('creatorid', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'creatorID')),
            ('inventorybasepermissions', self.gf('django.db.models.fields.IntegerField')(db_column=u'inventoryBasePermissions')),
            ('inventoryeveryonepermissions', self.gf('django.db.models.fields.IntegerField')(db_column=u'inventoryEveryOnePermissions')),
            ('saleprice', self.gf('django.db.models.fields.IntegerField')(db_column=u'salePrice')),
            ('saletype', self.gf('django.db.models.fields.IntegerField')(db_column=u'saleType')),
            ('creationdate', self.gf('django.db.models.fields.IntegerField')(db_column=u'creationDate')),
            ('groupid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'groupID')),
            ('groupowned', self.gf('django.db.models.fields.IntegerField')(db_column=u'groupOwned')),
            ('flags', self.gf('django.db.models.fields.IntegerField')()),
            ('inventoryid', self.gf('django.db.models.fields.CharField')(max_length=36L, primary_key=True, db_column=u'inventoryID')),
            ('avatarid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'avatarID', blank=True)),
            ('parentfolderid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'parentFolderID', blank=True)),
            ('inventorygrouppermissions', self.gf('django.db.models.fields.IntegerField')(db_column=u'inventoryGroupPermissions')),
        ))
        db.send_create_signal(u'grid_core', ['Inventoryitems'])

        # Adding model 'Migrations'
        db.create_table(u'migrations', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('version', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'grid_core', ['Migrations'])

        # Adding model 'OsGroupsGroups'
        db.create_table(u'os_groups_groups', (
            ('groupid', self.gf('django.db.models.fields.CharField')(max_length=36L, primary_key=True, db_column=u'GroupID')),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'Location')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'Name')),
            ('charter', self.gf('django.db.models.fields.TextField')(db_column=u'Charter')),
            ('insigniaid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'InsigniaID')),
            ('founderid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'FounderID')),
            ('membershipfee', self.gf('django.db.models.fields.IntegerField')(db_column=u'MembershipFee')),
            ('openenrollment', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'OpenEnrollment')),
            ('showinlist', self.gf('django.db.models.fields.IntegerField')(db_column=u'ShowInList')),
            ('allowpublish', self.gf('django.db.models.fields.IntegerField')(db_column=u'AllowPublish')),
            ('maturepublish', self.gf('django.db.models.fields.IntegerField')(db_column=u'MaturePublish')),
            ('ownerroleid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'OwnerRoleID')),
        ))
        db.send_create_signal(u'grid_core', ['OsGroupsGroups'])

        # Adding model 'OsGroupsInvites'
        db.create_table(u'os_groups_invites', (
            ('inviteid', self.gf('django.db.models.fields.CharField')(max_length=36L, primary_key=True, db_column=u'InviteID')),
            ('groupid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'GroupID')),
            ('roleid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'RoleID')),
            ('principalid', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'PrincipalID')),
            ('tmstamp', self.gf('django.db.models.fields.DateTimeField')(db_column=u'TMStamp')),
        ))
        db.send_create_signal(u'grid_core', ['OsGroupsInvites'])

        # Adding model 'OsGroupsMembership'
        db.create_table(u'os_groups_membership', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('groupid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'GroupID')),
            ('principalid', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'PrincipalID')),
            ('selectedroleid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'SelectedRoleID')),
            ('contribution', self.gf('django.db.models.fields.IntegerField')(db_column=u'Contribution')),
            ('listinprofile', self.gf('django.db.models.fields.IntegerField')(db_column=u'ListInProfile')),
            ('acceptnotices', self.gf('django.db.models.fields.IntegerField')(db_column=u'AcceptNotices')),
            ('accesstoken', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'AccessToken')),
        ))
        db.send_create_signal(u'grid_core', ['OsGroupsMembership'])

        # Adding model 'OsGroupsNotices'
        db.create_table(u'os_groups_notices', (
            ('groupid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'GroupID')),
            ('noticeid', self.gf('django.db.models.fields.CharField')(max_length=36L, primary_key=True, db_column=u'NoticeID')),
            ('tmstamp', self.gf('django.db.models.fields.IntegerField')(db_column=u'TMStamp')),
            ('fromname', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'FromName')),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'Subject')),
            ('message', self.gf('django.db.models.fields.TextField')(db_column=u'Message')),
            ('hasattachment', self.gf('django.db.models.fields.IntegerField')(db_column=u'HasAttachment')),
            ('attachmenttype', self.gf('django.db.models.fields.IntegerField')(db_column=u'AttachmentType')),
            ('attachmentname', self.gf('django.db.models.fields.CharField')(max_length=128L, db_column=u'AttachmentName')),
            ('attachmentitemid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'AttachmentItemID')),
            ('attachmentownerid', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'AttachmentOwnerID')),
        ))
        db.send_create_signal(u'grid_core', ['OsGroupsNotices'])

        # Adding model 'OsGroupsPrincipals'
        db.create_table(u'os_groups_principals', (
            ('principalid', self.gf('django.db.models.fields.CharField')(max_length=255L, primary_key=True, db_column=u'PrincipalID')),
            ('activegroupid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'ActiveGroupID')),
        ))
        db.send_create_signal(u'grid_core', ['OsGroupsPrincipals'])

        # Adding model 'OsGroupsRolemembership'
        db.create_table(u'os_groups_rolemembership', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('groupid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'GroupID')),
            ('roleid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'RoleID')),
            ('principalid', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'PrincipalID')),
        ))
        db.send_create_signal(u'grid_core', ['OsGroupsRolemembership'])

        # Adding model 'OsGroupsRoles'
        db.create_table(u'os_groups_roles', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('groupid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'GroupID')),
            ('roleid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'RoleID')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'Name')),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'Description')),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'Title')),
            ('powers', self.gf('django.db.models.fields.BigIntegerField')(db_column=u'Powers')),
        ))
        db.send_create_signal(u'grid_core', ['OsGroupsRoles'])

        # Adding model 'Regions'
        db.create_table(u'regions', (
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36L, primary_key=True)),
            ('regionhandle', self.gf('django.db.models.fields.BigIntegerField')(db_column=u'regionHandle')),
            ('regionname', self.gf('django.db.models.fields.CharField')(max_length=128L, db_column=u'regionName', blank=True)),
            ('regionrecvkey', self.gf('django.db.models.fields.CharField')(max_length=128L, db_column=u'regionRecvKey', blank=True)),
            ('regionsendkey', self.gf('django.db.models.fields.CharField')(max_length=128L, db_column=u'regionSendKey', blank=True)),
            ('regionsecret', self.gf('django.db.models.fields.CharField')(max_length=128L, db_column=u'regionSecret', blank=True)),
            ('regiondatauri', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'regionDataURI', blank=True)),
            ('serverip', self.gf('django.db.models.fields.CharField')(max_length=64L, db_column=u'serverIP', blank=True)),
            ('serverport', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'serverPort', blank=True)),
            ('serveruri', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'serverURI', blank=True)),
            ('locx', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'locX', blank=True)),
            ('locy', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'locY', blank=True)),
            ('locz', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'locZ', blank=True)),
            ('eastoverridehandle', self.gf('django.db.models.fields.BigIntegerField')(null=True, db_column=u'eastOverrideHandle', blank=True)),
            ('westoverridehandle', self.gf('django.db.models.fields.BigIntegerField')(null=True, db_column=u'westOverrideHandle', blank=True)),
            ('southoverridehandle', self.gf('django.db.models.fields.BigIntegerField')(null=True, db_column=u'southOverrideHandle', blank=True)),
            ('northoverridehandle', self.gf('django.db.models.fields.BigIntegerField')(null=True, db_column=u'northOverrideHandle', blank=True)),
            ('regionasseturi', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'regionAssetURI', blank=True)),
            ('regionassetrecvkey', self.gf('django.db.models.fields.CharField')(max_length=128L, db_column=u'regionAssetRecvKey', blank=True)),
            ('regionassetsendkey', self.gf('django.db.models.fields.CharField')(max_length=128L, db_column=u'regionAssetSendKey', blank=True)),
            ('regionuseruri', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'regionUserURI', blank=True)),
            ('regionuserrecvkey', self.gf('django.db.models.fields.CharField')(max_length=128L, db_column=u'regionUserRecvKey', blank=True)),
            ('regionusersendkey', self.gf('django.db.models.fields.CharField')(max_length=128L, db_column=u'regionUserSendKey', blank=True)),
            ('regionmaptexture', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'regionMapTexture', blank=True)),
            ('serverhttpport', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'serverHttpPort', blank=True)),
            ('serverremotingport', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'serverRemotingPort', blank=True)),
            ('owner_uuid', self.gf('django.db.models.fields.CharField')(max_length=36L)),
            ('originuuid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'originUUID', blank=True)),
            ('access', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('scopeid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'ScopeID')),
            ('sizex', self.gf('django.db.models.fields.IntegerField')(db_column=u'sizeX')),
            ('sizey', self.gf('django.db.models.fields.IntegerField')(db_column=u'sizeY')),
            ('flags', self.gf('django.db.models.fields.IntegerField')()),
            ('last_seen', self.gf('django.db.models.fields.IntegerField')()),
            ('principalid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'PrincipalID')),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=255L, db_column=u'Token')),
            ('parcelmaptexture', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'parcelMapTexture', blank=True)),
        ))
        db.send_create_signal(u'grid_core', ['Regions'])

        # Adding model 'Tokens'
        db.create_table(u'tokens', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36L, db_column=u'UUID')),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=255L)),
            ('validity', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'grid_core', ['Tokens'])


    def backwards(self, orm):
        # Deleting model 'Avatars'
        db.delete_table(u'Avatars')

        # Deleting model 'Friends'
        db.delete_table(u'Friends')

        # Deleting model 'Griduser'
        db.delete_table(u'GridUser')

        # Deleting model 'Presence'
        db.delete_table(u'Presence')

        # Deleting model 'Useraccounts'
        db.delete_table(u'UserAccounts')

        # Deleting model 'Auth'
        db.delete_table(u'auth')

        # Deleting model 'HgTravelingData'
        db.delete_table(u'hg_traveling_data')

        # Deleting model 'ImOffline'
        db.delete_table(u'im_offline')

        # Deleting model 'Inventoryfolders'
        db.delete_table(u'inventoryfolders')

        # Deleting model 'Inventoryitems'
        db.delete_table(u'inventoryitems')

        # Deleting model 'Migrations'
        db.delete_table(u'migrations')

        # Deleting model 'OsGroupsGroups'
        db.delete_table(u'os_groups_groups')

        # Deleting model 'OsGroupsInvites'
        db.delete_table(u'os_groups_invites')

        # Deleting model 'OsGroupsMembership'
        db.delete_table(u'os_groups_membership')

        # Deleting model 'OsGroupsNotices'
        db.delete_table(u'os_groups_notices')

        # Deleting model 'OsGroupsPrincipals'
        db.delete_table(u'os_groups_principals')

        # Deleting model 'OsGroupsRolemembership'
        db.delete_table(u'os_groups_rolemembership')

        # Deleting model 'OsGroupsRoles'
        db.delete_table(u'os_groups_roles')

        # Deleting model 'Regions'
        db.delete_table(u'regions')

        # Deleting model 'Tokens'
        db.delete_table(u'tokens')


    models = {
        u'grid_core.auth': {
            'Meta': {'object_name': 'Auth', 'db_table': "u'auth'"},
            'accounttype': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'db_column': "u'accountType'"}),
            'passwordhash': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'db_column': "u'passwordHash'"}),
            'passwordsalt': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'db_column': "u'passwordSalt'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'primary_key': 'True', 'db_column': "u'UUID'"}),
            'webloginkey': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'webLoginKey'"})
        },
        u'grid_core.avatars': {
            'Meta': {'object_name': 'Avatars', 'db_table': "u'Avatars'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'db_column': "u'Name'"}),
            'principalid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'PrincipalID'"}),
            'value': ('django.db.models.fields.TextField', [], {'db_column': "u'Value'", 'blank': 'True'})
        },
        u'grid_core.friends': {
            'Meta': {'object_name': 'Friends', 'db_table': "u'Friends'"},
            'flags': ('django.db.models.fields.CharField', [], {'max_length': '16L', 'db_column': "u'Flags'"}),
            'friend': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'Friend'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'offered': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'db_column': "u'Offered'"}),
            'principalid': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'PrincipalID'"})
        },
        u'grid_core.griduser': {
            'Meta': {'object_name': 'Griduser', 'db_table': "u'GridUser'"},
            'homelookat': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'db_column': "u'HomeLookAt'"}),
            'homeposition': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'db_column': "u'HomePosition'"}),
            'homeregionid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'HomeRegionID'"}),
            'lastlookat': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'db_column': "u'LastLookAt'"}),
            'lastposition': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'db_column': "u'LastPosition'"}),
            'lastregionid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'LastRegionID'"}),
            'login': ('django.db.models.fields.CharField', [], {'max_length': '16L', 'db_column': "u'Login'"}),
            'logout': ('django.db.models.fields.CharField', [], {'max_length': '16L', 'db_column': "u'Logout'"}),
            'online': ('django.db.models.fields.CharField', [], {'max_length': '5L', 'db_column': "u'Online'"}),
            'userid': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'primary_key': 'True', 'db_column': "u'UserID'"})
        },
        u'grid_core.hgtravelingdata': {
            'Meta': {'object_name': 'HgTravelingData', 'db_table': "u'hg_traveling_data'"},
            'clientipaddress': ('django.db.models.fields.CharField', [], {'max_length': '16L', 'db_column': "u'ClientIPAddress'"}),
            'gridexternalname': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'GridExternalName'"}),
            'myipaddress': ('django.db.models.fields.CharField', [], {'max_length': '16L', 'db_column': "u'MyIPAddress'"}),
            'servicetoken': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'ServiceToken'"}),
            'sessionid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'primary_key': 'True', 'db_column': "u'SessionID'"}),
            'tmstamp': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'TMStamp'"}),
            'userid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'UserID'"})
        },
        u'grid_core.imoffline': {
            'Meta': {'object_name': 'ImOffline', 'db_table': "u'im_offline'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'ID'"}),
            'message': ('django.db.models.fields.TextField', [], {'db_column': "u'Message'"}),
            'principalid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'PrincipalID'"}),
            'tmstamp': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'TMStamp'"})
        },
        u'grid_core.inventoryfolders': {
            'Meta': {'object_name': 'Inventoryfolders', 'db_table': "u'inventoryfolders'"},
            'agentid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'agentID'", 'blank': 'True'}),
            'folderid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'primary_key': 'True', 'db_column': "u'folderID'"}),
            'foldername': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'db_column': "u'folderName'", 'blank': 'True'}),
            'parentfolderid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'parentFolderID'", 'blank': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {}),
            'version': ('django.db.models.fields.IntegerField', [], {})
        },
        u'grid_core.inventoryitems': {
            'Meta': {'object_name': 'Inventoryitems', 'db_table': "u'inventoryitems'"},
            'assetid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'assetID'", 'blank': 'True'}),
            'assettype': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'assetType'", 'blank': 'True'}),
            'avatarid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'avatarID'", 'blank': 'True'}),
            'creationdate': ('django.db.models.fields.IntegerField', [], {'db_column': "u'creationDate'"}),
            'creatorid': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'creatorID'"}),
            'flags': ('django.db.models.fields.IntegerField', [], {}),
            'groupid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'groupID'"}),
            'groupowned': ('django.db.models.fields.IntegerField', [], {'db_column': "u'groupOwned'"}),
            'inventorybasepermissions': ('django.db.models.fields.IntegerField', [], {'db_column': "u'inventoryBasePermissions'"}),
            'inventorycurrentpermissions': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'inventoryCurrentPermissions'", 'blank': 'True'}),
            'inventorydescription': ('django.db.models.fields.CharField', [], {'max_length': '128L', 'db_column': "u'inventoryDescription'", 'blank': 'True'}),
            'inventoryeveryonepermissions': ('django.db.models.fields.IntegerField', [], {'db_column': "u'inventoryEveryOnePermissions'"}),
            'inventorygrouppermissions': ('django.db.models.fields.IntegerField', [], {'db_column': "u'inventoryGroupPermissions'"}),
            'inventoryid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'primary_key': 'True', 'db_column': "u'inventoryID'"}),
            'inventoryname': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'db_column': "u'inventoryName'", 'blank': 'True'}),
            'inventorynextpermissions': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'inventoryNextPermissions'", 'blank': 'True'}),
            'invtype': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'invType'", 'blank': 'True'}),
            'parentfolderid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'parentFolderID'", 'blank': 'True'}),
            'saleprice': ('django.db.models.fields.IntegerField', [], {'db_column': "u'salePrice'"}),
            'saletype': ('django.db.models.fields.IntegerField', [], {'db_column': "u'saleType'"})
        },
        u'grid_core.migrations': {
            'Meta': {'object_name': 'Migrations', 'db_table': "u'migrations'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'version': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'grid_core.osgroupsgroups': {
            'Meta': {'object_name': 'OsGroupsGroups', 'db_table': "u'os_groups_groups'"},
            'allowpublish': ('django.db.models.fields.IntegerField', [], {'db_column': "u'AllowPublish'"}),
            'charter': ('django.db.models.fields.TextField', [], {'db_column': "u'Charter'"}),
            'founderid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'FounderID'"}),
            'groupid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'primary_key': 'True', 'db_column': "u'GroupID'"}),
            'insigniaid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'InsigniaID'"}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'Location'"}),
            'maturepublish': ('django.db.models.fields.IntegerField', [], {'db_column': "u'MaturePublish'"}),
            'membershipfee': ('django.db.models.fields.IntegerField', [], {'db_column': "u'MembershipFee'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'Name'"}),
            'openenrollment': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'OpenEnrollment'"}),
            'ownerroleid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'OwnerRoleID'"}),
            'showinlist': ('django.db.models.fields.IntegerField', [], {'db_column': "u'ShowInList'"})
        },
        u'grid_core.osgroupsinvites': {
            'Meta': {'object_name': 'OsGroupsInvites', 'db_table': "u'os_groups_invites'"},
            'groupid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'GroupID'"}),
            'inviteid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'primary_key': 'True', 'db_column': "u'InviteID'"}),
            'principalid': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'PrincipalID'"}),
            'roleid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'RoleID'"}),
            'tmstamp': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'TMStamp'"})
        },
        u'grid_core.osgroupsmembership': {
            'Meta': {'object_name': 'OsGroupsMembership', 'db_table': "u'os_groups_membership'"},
            'acceptnotices': ('django.db.models.fields.IntegerField', [], {'db_column': "u'AcceptNotices'"}),
            'accesstoken': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'AccessToken'"}),
            'contribution': ('django.db.models.fields.IntegerField', [], {'db_column': "u'Contribution'"}),
            'groupid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'GroupID'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listinprofile': ('django.db.models.fields.IntegerField', [], {'db_column': "u'ListInProfile'"}),
            'principalid': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'PrincipalID'"}),
            'selectedroleid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'SelectedRoleID'"})
        },
        u'grid_core.osgroupsnotices': {
            'Meta': {'object_name': 'OsGroupsNotices', 'db_table': "u'os_groups_notices'"},
            'attachmentitemid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'AttachmentItemID'"}),
            'attachmentname': ('django.db.models.fields.CharField', [], {'max_length': '128L', 'db_column': "u'AttachmentName'"}),
            'attachmentownerid': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'AttachmentOwnerID'"}),
            'attachmenttype': ('django.db.models.fields.IntegerField', [], {'db_column': "u'AttachmentType'"}),
            'fromname': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'FromName'"}),
            'groupid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'GroupID'"}),
            'hasattachment': ('django.db.models.fields.IntegerField', [], {'db_column': "u'HasAttachment'"}),
            'message': ('django.db.models.fields.TextField', [], {'db_column': "u'Message'"}),
            'noticeid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'primary_key': 'True', 'db_column': "u'NoticeID'"}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'Subject'"}),
            'tmstamp': ('django.db.models.fields.IntegerField', [], {'db_column': "u'TMStamp'"})
        },
        u'grid_core.osgroupsprincipals': {
            'Meta': {'object_name': 'OsGroupsPrincipals', 'db_table': "u'os_groups_principals'"},
            'activegroupid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'ActiveGroupID'"}),
            'principalid': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'primary_key': 'True', 'db_column': "u'PrincipalID'"})
        },
        u'grid_core.osgroupsrolemembership': {
            'Meta': {'object_name': 'OsGroupsRolemembership', 'db_table': "u'os_groups_rolemembership'"},
            'groupid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'GroupID'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'principalid': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'PrincipalID'"}),
            'roleid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'RoleID'"})
        },
        u'grid_core.osgroupsroles': {
            'Meta': {'object_name': 'OsGroupsRoles', 'db_table': "u'os_groups_roles'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'Description'"}),
            'groupid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'GroupID'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'Name'"}),
            'powers': ('django.db.models.fields.BigIntegerField', [], {'db_column': "u'Powers'"}),
            'roleid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'RoleID'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'Title'"})
        },
        u'grid_core.presence': {
            'Meta': {'object_name': 'Presence', 'db_table': "u'Presence'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastseen': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'LastSeen'"}),
            'regionid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'RegionID'"}),
            'securesessionid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'SecureSessionID'"}),
            'sessionid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36L', 'db_column': "u'SessionID'"}),
            'userid': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'UserID'"})
        },
        u'grid_core.regions': {
            'Meta': {'object_name': 'Regions', 'db_table': "u'regions'"},
            'access': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'eastoverridehandle': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'db_column': "u'eastOverrideHandle'", 'blank': 'True'}),
            'flags': ('django.db.models.fields.IntegerField', [], {}),
            'last_seen': ('django.db.models.fields.IntegerField', [], {}),
            'locx': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'locX'", 'blank': 'True'}),
            'locy': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'locY'", 'blank': 'True'}),
            'locz': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'locZ'", 'blank': 'True'}),
            'northoverridehandle': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'db_column': "u'northOverrideHandle'", 'blank': 'True'}),
            'originuuid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'originUUID'", 'blank': 'True'}),
            'owner_uuid': ('django.db.models.fields.CharField', [], {'max_length': '36L'}),
            'parcelmaptexture': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'parcelMapTexture'", 'blank': 'True'}),
            'principalid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'PrincipalID'"}),
            'regionassetrecvkey': ('django.db.models.fields.CharField', [], {'max_length': '128L', 'db_column': "u'regionAssetRecvKey'", 'blank': 'True'}),
            'regionassetsendkey': ('django.db.models.fields.CharField', [], {'max_length': '128L', 'db_column': "u'regionAssetSendKey'", 'blank': 'True'}),
            'regionasseturi': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'regionAssetURI'", 'blank': 'True'}),
            'regiondatauri': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'regionDataURI'", 'blank': 'True'}),
            'regionhandle': ('django.db.models.fields.BigIntegerField', [], {'db_column': "u'regionHandle'"}),
            'regionmaptexture': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'regionMapTexture'", 'blank': 'True'}),
            'regionname': ('django.db.models.fields.CharField', [], {'max_length': '128L', 'db_column': "u'regionName'", 'blank': 'True'}),
            'regionrecvkey': ('django.db.models.fields.CharField', [], {'max_length': '128L', 'db_column': "u'regionRecvKey'", 'blank': 'True'}),
            'regionsecret': ('django.db.models.fields.CharField', [], {'max_length': '128L', 'db_column': "u'regionSecret'", 'blank': 'True'}),
            'regionsendkey': ('django.db.models.fields.CharField', [], {'max_length': '128L', 'db_column': "u'regionSendKey'", 'blank': 'True'}),
            'regionuserrecvkey': ('django.db.models.fields.CharField', [], {'max_length': '128L', 'db_column': "u'regionUserRecvKey'", 'blank': 'True'}),
            'regionusersendkey': ('django.db.models.fields.CharField', [], {'max_length': '128L', 'db_column': "u'regionUserSendKey'", 'blank': 'True'}),
            'regionuseruri': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'regionUserURI'", 'blank': 'True'}),
            'scopeid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'ScopeID'"}),
            'serverhttpport': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'serverHttpPort'", 'blank': 'True'}),
            'serverip': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'db_column': "u'serverIP'", 'blank': 'True'}),
            'serverport': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'serverPort'", 'blank': 'True'}),
            'serverremotingport': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'serverRemotingPort'", 'blank': 'True'}),
            'serveruri': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'serverURI'", 'blank': 'True'}),
            'sizex': ('django.db.models.fields.IntegerField', [], {'db_column': "u'sizeX'"}),
            'sizey': ('django.db.models.fields.IntegerField', [], {'db_column': "u'sizeY'"}),
            'southoverridehandle': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'db_column': "u'southOverrideHandle'", 'blank': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'Token'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'primary_key': 'True'}),
            'westoverridehandle': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'db_column': "u'westOverrideHandle'", 'blank': 'True'})
        },
        u'grid_core.tokens': {
            'Meta': {'object_name': 'Tokens', 'db_table': "u'tokens'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255L'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'UUID'"}),
            'validity': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'grid_core.useraccounts': {
            'Meta': {'object_name': 'Useraccounts', 'db_table': "u'UserAccounts'"},
            'created': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Created'", 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'db_column': "u'Email'", 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'db_column': "u'FirstName'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'db_column': "u'LastName'"}),
            'principalid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36L', 'db_column': "u'PrincipalID'"}),
            'scopeid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'ScopeID'"}),
            'serviceurls': ('django.db.models.fields.TextField', [], {'db_column': "u'ServiceURLs'", 'blank': 'True'}),
            'userflags': ('django.db.models.fields.IntegerField', [], {'db_column': "u'UserFlags'"}),
            'userlevel': ('django.db.models.fields.IntegerField', [], {'db_column': "u'UserLevel'"}),
            'usertitle': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'db_column': "u'UserTitle'"})
        }
    }

    complete_apps = ['grid_core']