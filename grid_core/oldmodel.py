from __future__ import unicode_literals

from django.db import models

class Avatars(models.Model):
    avatarid = models.AutoField(primary_key=True, db_column='AvatarID') #Newly added
    principalid = models.CharField(max_length=36L, db_column='PrincipalID') 
    name = models.CharField(max_length=32L, db_column='Name') 
    value = models.TextField(db_column='Value', blank=True) 
    class Meta:
        db_table = 'Avatars'

class Friends(models.Model):
    friendid = models.AutoField(primary_key=True, 'FriendID') #Newly added
    principalid = models.CharField(max_length=255L, db_column='PrincipalID') 
    friend = models.CharField(max_length=255L, db_column='Friend') 
    flags = models.CharField(max_length=16L, db_column='Flags') 
    offered = models.CharField(max_length=32L, db_column='Offered') 
    class Meta:
        db_table = 'Friends'

class Griduser(models.Model):
    userid = models.CharField(max_length=255L, primary_key=True, db_column='UserID') 
    homeregionid = models.CharField(max_length=36L, db_column='HomeRegionID') 
    homeposition = models.CharField(max_length=64L, db_column='HomePosition') 
    homelookat = models.CharField(max_length=64L, db_column='HomeLookAt') 
    lastregionid = models.CharField(max_length=36L, db_column='LastRegionID') 
    lastposition = models.CharField(max_length=64L, db_column='LastPosition') 
    lastlookat = models.CharField(max_length=64L, db_column='LastLookAt') 
    online = models.CharField(max_length=5L, db_column='Online') 
    login = models.CharField(max_length=16L, db_column='Login') 
    logout = models.CharField(max_length=16L, db_column='Logout') 
    class Meta:
        db_table = 'GridUser'

class Presence(models.Model):
    presenceid = models.AutoField(primary_key=True, db_column='PresenceID') #Newly added
    userid = models.CharField(max_length=255L, db_column='UserID') 
    regionid = models.CharField(max_length=36L, db_column='RegionID') 
    sessionid = models.CharField(max_length=36L, unique=True, db_column='SessionID') 
    securesessionid = models.CharField(max_length=36L, db_column='SecureSessionID') 
    lastseen = models.DateTimeField(db_column='LastSeen') 
    class Meta:
        db_table = 'Presence'

class Useraccounts(models.Model):
    useraccountid = models.AutoField(primary_key=True, db_column='UserAccountID') #Newly added
    principalid = models.CharField(max_length=36L, unique=True, db_column='PrincipalID') 
    scopeid = models.CharField(max_length=36L, db_column='ScopeID') 
    firstname = models.CharField(max_length=64L, db_column='FirstName') 
    lastname = models.CharField(max_length=64L, db_column='LastName') 
    email = models.CharField(max_length=64L, db_column='Email', blank=True) 
    serviceurls = models.TextField(db_column='ServiceURLs', blank=True) 
    created = models.IntegerField(null=True, db_column='Created', blank=True) 
    userlevel = models.IntegerField(db_column='UserLevel') 
    userflags = models.IntegerField(db_column='UserFlags') 
    usertitle = models.CharField(max_length=64L, db_column='UserTitle') 
    class Meta:
        db_table = 'UserAccounts'

class Auth(models.Model):
    uuid = models.CharField(max_length=36L, primary_key=True, db_column='UUID') 
    passwordhash = models.CharField(max_length=32L, db_column='passwordHash') 
    passwordsalt = models.CharField(max_length=32L, db_column='passwordSalt') 
    webloginkey = models.CharField(max_length=255L, db_column='webLoginKey') 
    accounttype = models.CharField(max_length=32L, db_column='accountType') 
    class Meta:
        db_table = 'auth'

class HgTravelingData(models.Model):
    sessionid = models.CharField(max_length=36L, primary_key=True, db_column='SessionID') 
    userid = models.CharField(max_length=36L, db_column='UserID') 
    gridexternalname = models.CharField(max_length=255L, db_column='GridExternalName') 
    servicetoken = models.CharField(max_length=255L, db_column='ServiceToken') 
    clientipaddress = models.CharField(max_length=16L, db_column='ClientIPAddress') 
    myipaddress = models.CharField(max_length=16L, db_column='MyIPAddress') 
    tmstamp = models.DateTimeField(db_column='TMStamp') 
    class Meta:
        db_table = 'hg_traveling_data'

class ImOffline(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') 
    principalid = models.CharField(max_length=36L, db_column='PrincipalID') 
    message = models.TextField(db_column='Message') 
    tmstamp = models.DateTimeField(db_column='TMStamp') 
    class Meta:
        db_table = 'im_offline'

class Inventoryfolders(models.Model):
    foldername = models.CharField(max_length=64L, db_column='folderName', blank=True) 
    type = models.IntegerField()
    version = models.IntegerField()
    folderid = models.CharField(max_length=36L, primary_key=True, db_column='folderID') 
    agentid = models.CharField(max_length=36L, db_column='agentID', blank=True) 
    parentfolderid = models.CharField(max_length=36L, db_column='parentFolderID', blank=True) 
    class Meta:
        db_table = 'inventoryfolders'

class Inventoryitems(models.Model):
    assetid = models.CharField(max_length=36L, db_column='assetID', blank=True) 
    assettype = models.IntegerField(null=True, db_column='assetType', blank=True) 
    inventoryname = models.CharField(max_length=64L, db_column='inventoryName', blank=True) 
    inventorydescription = models.CharField(max_length=128L, db_column='inventoryDescription', blank=True) 
    inventorynextpermissions = models.IntegerField(null=True, db_column='inventoryNextPermissions', blank=True) 
    inventorycurrentpermissions = models.IntegerField(null=True, db_column='inventoryCurrentPermissions', blank=True) 
    invtype = models.IntegerField(null=True, db_column='invType', blank=True) 
    creatorid = models.CharField(max_length=255L, db_column='creatorID') 
    inventorybasepermissions = models.IntegerField(db_column='inventoryBasePermissions') 
    inventoryeveryonepermissions = models.IntegerField(db_column='inventoryEveryOnePermissions') 
    saleprice = models.IntegerField(db_column='salePrice') 
    saletype = models.IntegerField(db_column='saleType') 
    creationdate = models.IntegerField(db_column='creationDate') 
    groupid = models.CharField(max_length=36L, db_column='groupID') 
    groupowned = models.IntegerField(db_column='groupOwned') 
    flags = models.IntegerField()
    inventoryid = models.CharField(max_length=36L, primary_key=True, db_column='inventoryID') 
    avatarid = models.CharField(max_length=36L, db_column='avatarID', blank=True) 
    parentfolderid = models.CharField(max_length=36L, db_column='parentFolderID', blank=True) 
    inventorygrouppermissions = models.IntegerField(db_column='inventoryGroupPermissions') 
    class Meta:
        db_table = 'inventoryitems'

class Migrations(models.Model):
    migrationid = models.AutoField(primary_key=True, db_column='MigrationID') #Newly added
    name = models.CharField(max_length=100L, blank=True)
    version = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'migrations'

class OsGroupsGroups(models.Model):
    groupid = models.CharField(max_length=36L, primary_key=True, db_column='GroupID') 
    location = models.CharField(max_length=255L, db_column='Location') 
    name = models.CharField(max_length=255L, db_column='Name') 
    charter = models.TextField(db_column='Charter') 
    insigniaid = models.CharField(max_length=36L, db_column='InsigniaID') 
    founderid = models.CharField(max_length=36L, db_column='FounderID') 
    membershipfee = models.IntegerField(db_column='MembershipFee') 
    openenrollment = models.CharField(max_length=255L, db_column='OpenEnrollment') 
    showinlist = models.IntegerField(db_column='ShowInList') 
    allowpublish = models.IntegerField(db_column='AllowPublish') 
    maturepublish = models.IntegerField(db_column='MaturePublish') 
    ownerroleid = models.CharField(max_length=36L, db_column='OwnerRoleID') 
    class Meta:
        db_table = 'os_groups_groups'

class OsGroupsInvites(models.Model):
    inviteid = models.CharField(max_length=36L, primary_key=True, db_column='InviteID') 
    groupid = models.CharField(max_length=36L, db_column='GroupID') 
    roleid = models.CharField(max_length=36L, db_column='RoleID') 
    principalid = models.CharField(max_length=255L, db_column='PrincipalID') 
    tmstamp = models.DateTimeField(db_column='TMStamp') 
    class Meta:
        db_table = 'os_groups_invites'

class OsGroupsMembership(models.Model):
    groupmembershipid = models.AutoField(primary_key=True, db_column='GroupMembershipID') #Newly added
    groupid = models.CharField(max_length=36L, db_column='GroupID') 
    principalid = models.CharField(max_length=255L, db_column='PrincipalID') 
    selectedroleid = models.CharField(max_length=36L, db_column='SelectedRoleID') 
    contribution = models.IntegerField(db_column='Contribution') 
    listinprofile = models.IntegerField(db_column='ListInProfile') 
    acceptnotices = models.IntegerField(db_column='AcceptNotices') 
    accesstoken = models.CharField(max_length=36L, db_column='AccessToken') 
    class Meta:
        db_table = 'os_groups_membership'

class OsGroupsNotices(models.Model):
    groupid = models.CharField(max_length=36L, db_column='GroupID') 
    noticeid = models.CharField(max_length=36L, primary_key=True, db_column='NoticeID') 
    tmstamp = models.IntegerField(db_column='TMStamp') 
    fromname = models.CharField(max_length=255L, db_column='FromName') 
    subject = models.CharField(max_length=255L, db_column='Subject') 
    message = models.TextField(db_column='Message') 
    hasattachment = models.IntegerField(db_column='HasAttachment') 
    attachmenttype = models.IntegerField(db_column='AttachmentType') 
    attachmentname = models.CharField(max_length=128L, db_column='AttachmentName') 
    attachmentitemid = models.CharField(max_length=36L, db_column='AttachmentItemID') 
    attachmentownerid = models.CharField(max_length=255L, db_column='AttachmentOwnerID') 
    class Meta:
        db_table = 'os_groups_notices'

class OsGroupsPrincipals(models.Model):
    principalid = models.CharField(max_length=255L, primary_key=True, db_column='PrincipalID') 
    activegroupid = models.CharField(max_length=36L, db_column='ActiveGroupID') 
    class Meta:
        db_table = 'os_groups_principals'

class OsGroupsRolemembership(models.Model):
    grouprolemembershipid = models.AutoField(primary_key=True, db_column='GroupRoleMembershipID') #Newly added
    groupid = models.CharField(max_length=36L, db_column='GroupID') 
    roleid = models.CharField(max_length=36L, db_column='RoleID') 
    principalid = models.CharField(max_length=255L, db_column='PrincipalID') 
    class Meta:
        db_table = 'os_groups_rolemembership'

class OsGroupsRoles(models.Model):
    grouproleid = models.AutoField(primary_key=True, db_column='GroupRoleID') #Newly added
    groupid = models.CharField(max_length=36L, db_column='GroupID',primary_key=False) 
    roleid = models.CharField(max_length=36L, db_column='RoleID',primary_key=False) 
    name = models.CharField(max_length=255L, db_column='Name') 
    description = models.CharField(max_length=255L, db_column='Description') 
    title = models.CharField(max_length=255L, db_column='Title') 
    powers = models.BigIntegerField(db_column='Powers') 
    class Meta:
        db_table = 'os_groups_roles'

    def __str__(self):
        return self.groupid

class Regions(models.Model):
    uuid = models.CharField(max_length=36L, primary_key=True)
    regionhandle = models.BigIntegerField(db_column='regionHandle') 
    regionname = models.CharField(max_length=128L, db_column='regionName', blank=True) 
    regionrecvkey = models.CharField(max_length=128L, db_column='regionRecvKey', blank=True) 
    regionsendkey = models.CharField(max_length=128L, db_column='regionSendKey', blank=True) 
    regionsecret = models.CharField(max_length=128L, db_column='regionSecret', blank=True) 
    regiondatauri = models.CharField(max_length=255L, db_column='regionDataURI', blank=True) 
    serverip = models.CharField(max_length=64L, db_column='serverIP', blank=True) 
    serverport = models.IntegerField(null=True, db_column='serverPort', blank=True) 
    serveruri = models.CharField(max_length=255L, db_column='serverURI', blank=True) 
    locx = models.IntegerField(null=True, db_column='locX', blank=True) 
    locy = models.IntegerField(null=True, db_column='locY', blank=True) 
    locz = models.IntegerField(null=True, db_column='locZ', blank=True) 
    eastoverridehandle = models.BigIntegerField(null=True, db_column='eastOverrideHandle', blank=True) 
    westoverridehandle = models.BigIntegerField(null=True, db_column='westOverrideHandle', blank=True) 
    southoverridehandle = models.BigIntegerField(null=True, db_column='southOverrideHandle', blank=True) 
    northoverridehandle = models.BigIntegerField(null=True, db_column='northOverrideHandle', blank=True) 
    regionasseturi = models.CharField(max_length=255L, db_column='regionAssetURI', blank=True) 
    regionassetrecvkey = models.CharField(max_length=128L, db_column='regionAssetRecvKey', blank=True) 
    regionassetsendkey = models.CharField(max_length=128L, db_column='regionAssetSendKey', blank=True) 
    regionuseruri = models.CharField(max_length=255L, db_column='regionUserURI', blank=True) 
    regionuserrecvkey = models.CharField(max_length=128L, db_column='regionUserRecvKey', blank=True) 
    regionusersendkey = models.CharField(max_length=128L, db_column='regionUserSendKey', blank=True) 
    regionmaptexture = models.CharField(max_length=36L, db_column='regionMapTexture', blank=True) 
    serverhttpport = models.IntegerField(null=True, db_column='serverHttpPort', blank=True) 
    serverremotingport = models.IntegerField(null=True, db_column='serverRemotingPort', blank=True) 
    owner_uuid = models.CharField(max_length=36L)
    originuuid = models.CharField(max_length=36L, db_column='originUUID', blank=True) 
    access = models.IntegerField(null=True, blank=True)
    scopeid = models.CharField(max_length=36L, db_column='ScopeID') 
    sizex = models.IntegerField(db_column='sizeX') 
    sizey = models.IntegerField(db_column='sizeY') 
    flags = models.IntegerField()
    last_seen = models.IntegerField()
    principalid = models.CharField(max_length=36L, db_column='PrincipalID') 
    token = models.CharField(max_length=255L, db_column='Token') 
    parcelmaptexture = models.CharField(max_length=36L, db_column='parcelMapTexture', blank=True) 
    class Meta:
        db_table = 'regions'

class Tokens(models.Model):
    tokenid = models.AutoField(primary_key=True, db_column='TokenID') #Newly added
    uuid = models.CharField(max_length=36L, db_column='UUID') 
    token = models.CharField(max_length=255L)
    validity = models.DateTimeField()
    class Meta:
        db_table = 'tokens'