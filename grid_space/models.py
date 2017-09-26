from __future__ import unicode_literals

from django.db import models


class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100L)
    name = models.CharField(max_length=50L)

    class Meta:
        db_table = 'django_site'


class GridSpaceConfigversion(models.Model):
    version = models.CharField(max_length=36L, primary_key=True)
    description = models.CharField(max_length=255L)

    class Meta:
        db_table = 'grid_space_configversion'


class GridSpaceGridenvironment(models.Model):
    id = models.IntegerField(primary_key=True)
    section = models.CharField(max_length=32L)
    entry = models.CharField(max_length=64L)
    value = models.CharField(max_length=255L)

    class Meta:
        db_table = 'grid_space_gridenvironment'


class GridSpaceHost(models.Model):
    host_key = models.CharField(max_length=36L, primary_key=True)
    host_name = models.CharField(max_length=255L, unique=True)
    host_ip = models.CharField(max_length=15L, unique=True)
    host_allowed = models.IntegerField()
    host_status = models.IntegerField()

    class Meta:
        db_table = 'grid_space_host'


class GridSpaceMainconfig(models.Model):
    id = models.IntegerField(primary_key=True)
    version = models.ForeignKey(GridSpaceConfigversion)
    section = models.CharField(max_length=32L)
    entry = models.CharField(max_length=64L)
    value = models.CharField(max_length=255L)

    class Meta:
        db_table = 'grid_space_mainconfig'


class GridSpaceRegionconfig(models.Model):
    id = models.IntegerField(primary_key=True)
    zone = models.ForeignKey('GridSpaceZone')
    enabled = models.IntegerField()
    access_state = models.CharField(max_length=32L)
    sim_name = models.CharField(max_length=255L, unique=True)
    # Field name made lowercase.
    sim_uuid = models.CharField(max_length=36L, db_column='sim_UUID')
    sim_location_x = models.CharField(max_length=16L)
    sim_location_y = models.CharField(max_length=16L)
    scope_id = models.CharField(max_length=36L)
    region_type = models.CharField(max_length=64L)
    internal_ip_address = models.CharField(max_length=16L)
    external_host_name = models.CharField(max_length=64L)
    internal_ip_port = models.CharField(max_length=12L)
    allow_alternate_ports = models.IntegerField()
    lastmap_uuid = models.CharField(max_length=36L)
    region_static_maptile = models.CharField(max_length=36L)
    lastmap_refresh = models.IntegerField()
    nonphysical_prim_max = models.CharField(max_length=4L)
    physical_prim_max = models.CharField(max_length=4L)
    clamp_prim_size = models.IntegerField()
    object_capactiy = models.CharField(max_length=8L)
    linkset_capactiy = models.CharField(max_length=8L)
    agent_capacity = models.CharField(max_length=3L)

    class Meta:
        db_table = 'grid_space_regionconfig'


class GridSpaceZone(models.Model):
    host = models.ForeignKey(GridSpaceHost)
    zone_key = models.CharField(max_length=36L, primary_key=True)
    name = models.CharField(max_length=64L)
    master_config = models.ForeignKey(GridSpaceConfigversion)
    control = models.CharField(max_length=1L)
    status = models.CharField(max_length=1L)
    inimaster = models.CharField(max_length=512L)
    inifile = models.CharField(max_length=512L)
    http_listener_port = models.CharField(max_length=5L)
    xmlrpc_port = models.CharField(max_length=5L)
    estate_database = models.CharField(max_length=64L)
    estate_datasource = models.CharField(max_length=255L)
    estate_database_port = models.CharField(max_length=6L)
    estate_database_user = models.CharField(max_length=64L)
    estate_database_password = models.CharField(max_length=64L)
    login_disable = models.IntegerField()

    class Meta:
        db_table = 'grid_space_zone'


class GridSpaceZoneconfig(models.Model):
    id = models.IntegerField(primary_key=True)
    zone = models.ForeignKey(GridSpaceZone)
    section = models.CharField(max_length=32L)
    entry = models.CharField(max_length=64L)
    value = models.CharField(max_length=255L)

    class Meta:
        db_table = 'grid_space_zoneconfig'


class LivesettingsLongsetting(models.Model):
    id = models.IntegerField(primary_key=True)
    site = models.ForeignKey(DjangoSite)
    group = models.CharField(max_length=100L)
    key = models.CharField(max_length=100L)
    value = models.TextField()

    class Meta:
        db_table = 'livesettings_longsetting'


class LivesettingsSetting(models.Model):
    id = models.IntegerField(primary_key=True)
    site = models.ForeignKey(DjangoSite)
    group = models.CharField(max_length=100L)
    key = models.CharField(max_length=100L)
    value = models.CharField(max_length=255L)

    class Meta:
        db_table = 'livesettings_setting'
