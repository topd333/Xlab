from __future__ import unicode_literals

from django.db import models


class EstateGroups(models.Model):
    estategroupid = models.AutoField(
        primary_key=True, db_column='EstateGroupID')  # Newly added
    estateid = models.IntegerField(db_column='EstateID')
    uuid = models.CharField(max_length=36L)

    class Meta:
        db_table = 'estate_groups'


class EstateManagers(models.Model):
    estatemanagerid = models.AutoField(
        primary_key=True, db_column='EstateManagerID')  # Newly added
    estateid = models.IntegerField(db_column='EstateID')
    uuid = models.CharField(max_length=36L)

    class Meta:
        db_table = 'estate_managers'


class EstateMap(models.Model):
    regionid = models.CharField(
        max_length=36L, primary_key=True, db_column='RegionID')
    estateid = models.IntegerField(db_column='EstateID')

    class Meta:
        db_table = 'estate_map'


class EstateSettings(models.Model):
    estateid = models.IntegerField(primary_key=True, db_column='EstateID')
    estatename = models.CharField(
        max_length=64L, db_column='EstateName', blank=True)
    abuseemailtoestateowner = models.IntegerField(
        db_column='AbuseEmailToEstateOwner')
    denyanonymous = models.IntegerField(db_column='DenyAnonymous')
    resethomeonteleport = models.IntegerField(db_column='ResetHomeOnTeleport')
    fixedsun = models.IntegerField(db_column='FixedSun')
    denytransacted = models.IntegerField(db_column='DenyTransacted')
    blockdwell = models.IntegerField(db_column='BlockDwell')
    denyidentified = models.IntegerField(db_column='DenyIdentified')
    allowvoice = models.IntegerField(db_column='AllowVoice')
    useglobaltime = models.IntegerField(db_column='UseGlobalTime')
    pricepermeter = models.IntegerField(db_column='PricePerMeter')
    taxfree = models.IntegerField(db_column='TaxFree')
    allowdirectteleport = models.IntegerField(db_column='AllowDirectTeleport')
    redirectgridx = models.IntegerField(db_column='RedirectGridX')
    redirectgridy = models.IntegerField(db_column='RedirectGridY')
    parentestateid = models.IntegerField(db_column='ParentEstateID')
    sunposition = models.FloatField(db_column='SunPosition')
    estateskipscripts = models.IntegerField(db_column='EstateSkipScripts')
    billablefactor = models.FloatField(db_column='BillableFactor')
    publicaccess = models.IntegerField(db_column='PublicAccess')
    abuseemail = models.CharField(max_length=255L, db_column='AbuseEmail')
    estateowner = models.CharField(max_length=36L, db_column='EstateOwner')
    denyminors = models.IntegerField(db_column='DenyMinors')
    allowlandmark = models.IntegerField(db_column='AllowLandmark')
    allowparcelchanges = models.IntegerField(db_column='AllowParcelChanges')
    allowsethome = models.IntegerField(db_column='AllowSetHome')

    class Meta:
        db_table = 'estate_settings'


class EstateUsers(models.Model):
    estateuserid = models.AutoField(
        primary_key=True, db_column='EstateUserID')  # Newly added
    estateid = models.IntegerField(db_column='EstateID')
    uuid = models.CharField(max_length=36L)

    class Meta:
        db_table = 'estate_users'


class Estateban(models.Model):
    estatebanid = models.AutoField(
        primary_key=True, db_column='EstateBanID')  # Newly added
    estateid = models.IntegerField(db_column='EstateID')
    banneduuid = models.CharField(max_length=36L, db_column='bannedUUID')
    bannedip = models.CharField(max_length=16L, db_column='bannedIp')
    bannediphostmask = models.CharField(
        max_length=16L, db_column='bannedIpHostMask')
    bannednamemask = models.CharField(
        max_length=64L, db_column='bannedNameMask', blank=True)

    class Meta:
        db_table = 'estateban'


class Migrations(models.Model):
    migrationid = models.AutoField(
        primary_key=True, db_column='migrationid')  # Newly added
    name = models.CharField(max_length=100L, blank=True)
    version = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'migrations'
