# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Avatars.id'
        #db.delete_column(u'Avatars', u'id')

        # Adding field 'Avatars.avatarid'
        db.add_column(u'Avatars', 'avatarid',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True, db_column=u'AvatarID'),
                      keep_default=False)

        # Deleting field 'Presence.id'
        #db.delete_column(u'Presence', u'id')

        # Adding field 'Presence.presenceid'
        db.add_column(u'Presence', 'presenceid',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True, db_column=u'PresenceID'),
                      keep_default=False)

        # Deleting field 'OsGroupsRoles.id'
        #db.delete_column(u'os_groups_roles', u'id')

        # Adding field 'OsGroupsRoles.grouproleid'
        db.add_column(u'os_groups_roles', 'grouproleid',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True, db_column=u'GroupRoleID'),
                      keep_default=False)

        # Deleting field 'Friends.id'
        #db.delete_column(u'Friends', u'id')

        # Adding field 'Friends.friendid'
        db.add_column(u'Friends', 'friendid',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True, db_column=u'FriendID'),
                      keep_default=False)

        # Deleting field 'Tokens.id'
        #db.delete_column(u'tokens', u'id')

        # Adding field 'Tokens.tokenid'
        db.add_column(u'tokens', 'tokenid',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True, db_column=u'TokenID'),
                      keep_default=False)

        # Deleting field 'OsGroupsRolemembership.id'
        #db.delete_column(u'os_groups_rolemembership', u'id')

        # Adding field 'OsGroupsRolemembership.grouprolemembershipid'
        db.add_column(u'os_groups_rolemembership', 'grouprolemembershipid',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True, db_column=u'GroupRoleMembershipID'),
                      keep_default=False)

        # Deleting field 'OsGroupsMembership.id'
        #db.delete_column(u'os_groups_membership', u'id')

        # Adding field 'OsGroupsMembership.groupmembershipid'
        db.add_column(u'os_groups_membership', 'groupmembershipid',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True, db_column=u'GroupMembershipID'),
                      keep_default=False)

        # Deleting field 'Useraccounts.id'
        #db.delete_column(u'UserAccounts', u'id')

        # Adding field 'Useraccounts.useraccountid'
        db.add_column(u'UserAccounts', 'useraccountid',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True, db_column=u'UserAccountID'),
                      keep_default=False)

        # Deleting field 'Migrations.id'
        #db.delete_column(u'migrations', u'id')

        # Adding field 'Migrations.migrationid'
        db.add_column(u'migrations', 'migrationid',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True, db_column=u'MigrationID'),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Avatars.id'
        db.add_column(u'Avatars', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True),
                      keep_default=False)

        # Deleting field 'Avatars.avatarid'
        db.delete_column(u'Avatars', u'AvatarID')

        # Adding field 'Presence.id'
        db.add_column(u'Presence', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True),
                      keep_default=False)

        # Deleting field 'Presence.presenceid'
        db.delete_column(u'Presence', u'PresenceID')

        # Adding field 'OsGroupsRoles.id'
        db.add_column(u'os_groups_roles', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True),
                      keep_default=False)

        # Deleting field 'OsGroupsRoles.grouproleid'
        db.delete_column(u'os_groups_roles', u'GroupRoleID')

        # Adding field 'Friends.id'
        db.add_column(u'Friends', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True),
                      keep_default=False)

        # Deleting field 'Friends.friendid'
        db.delete_column(u'Friends', u'FriendID')

        # Adding field 'Tokens.id'
        db.add_column(u'tokens', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True),
                      keep_default=False)

        # Deleting field 'Tokens.tokenid'
        db.delete_column(u'tokens', u'TokenID')

        # Adding field 'OsGroupsRolemembership.id'
        db.add_column(u'os_groups_rolemembership', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True),
                      keep_default=False)

        # Deleting field 'OsGroupsRolemembership.grouprolemembershipid'
        db.delete_column(u'os_groups_rolemembership', u'GroupRoleMembershipID')

        # Adding field 'OsGroupsMembership.id'
        db.add_column(u'os_groups_membership', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True),
                      keep_default=False)

        # Deleting field 'OsGroupsMembership.groupmembershipid'
        db.delete_column(u'os_groups_membership', u'GroupMembershipID')

        # Adding field 'Useraccounts.id'
        db.add_column(u'UserAccounts', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True),
                      keep_default=False)

        # Deleting field 'Useraccounts.useraccountid'
        db.delete_column(u'UserAccounts', u'UserAccountID')

        # Adding field 'Migrations.id'
        db.add_column(u'migrations', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True),
                      keep_default=False)

        # Deleting field 'Migrations.migrationid'
        db.delete_column(u'migrations', u'MigrationID')


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
            'avatarid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'AvatarID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'db_column': "u'Name'"}),
            'principalid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'PrincipalID'"}),
            'value': ('django.db.models.fields.TextField', [], {'db_column': "u'Value'", 'blank': 'True'})
        },
        u'grid_core.friends': {
            'Meta': {'object_name': 'Friends', 'db_table': "u'Friends'"},
            'flags': ('django.db.models.fields.CharField', [], {'max_length': '16L', 'db_column': "u'Flags'"}),
            'friend': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'Friend'"}),
            'friendid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'FriendID'"}),
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
            'migrationid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'MigrationID'"}),
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
            'groupmembershipid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'GroupMembershipID'"}),
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
            'grouprolemembershipid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'GroupRoleMembershipID'"}),
            'principalid': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'PrincipalID'"}),
            'roleid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'RoleID'"})
        },
        u'grid_core.osgroupsroles': {
            'Meta': {'object_name': 'OsGroupsRoles', 'db_table': "u'os_groups_roles'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'Description'"}),
            'groupid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'GroupID'"}),
            'grouproleid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'GroupRoleID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'Name'"}),
            'powers': ('django.db.models.fields.BigIntegerField', [], {'db_column': "u'Powers'"}),
            'roleid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'RoleID'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255L', 'db_column': "u'Title'"})
        },
        u'grid_core.presence': {
            'Meta': {'object_name': 'Presence', 'db_table': "u'Presence'"},
            'lastseen': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'LastSeen'"}),
            'presenceid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'PresenceID'"}),
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
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255L'}),
            'tokenid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'TokenID'"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'UUID'"}),
            'validity': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'grid_core.useraccounts': {
            'Meta': {'object_name': 'Useraccounts', 'db_table': "u'UserAccounts'"},
            'created': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Created'", 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'db_column': "u'Email'", 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'db_column': "u'FirstName'"}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'db_column': "u'LastName'"}),
            'principalid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36L', 'db_column': "u'PrincipalID'"}),
            'scopeid': ('django.db.models.fields.CharField', [], {'max_length': '36L', 'db_column': "u'ScopeID'"}),
            'serviceurls': ('django.db.models.fields.TextField', [], {'db_column': "u'ServiceURLs'", 'blank': 'True'}),
            'useraccountid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'UserAccountID'"}),
            'userflags': ('django.db.models.fields.IntegerField', [], {'db_column': "u'UserFlags'"}),
            'userlevel': ('django.db.models.fields.IntegerField', [], {'db_column': "u'UserLevel'"}),
            'usertitle': ('django.db.models.fields.CharField', [], {'max_length': '64L', 'db_column': "u'UserTitle'"})
        }
    }

    complete_apps = ['grid_core']