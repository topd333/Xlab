from django.db import models
from grid_user.models import User

# class Classifieds(models.Model):
#     classifieduuid = models.CharField(max_length=36L, primary_key=True)
#     creatoruuid = models.CharField(max_length=36L)
#     creationdate = models.IntegerField()
#     expirationdate = models.IntegerField()
#     category = models.CharField(max_length=20L)
#     name = models.CharField(max_length=255L)
#     description = models.TextField()
#     parceluuid = models.CharField(max_length=36L)
#     parentestate = models.IntegerField()
#     snapshotuuid = models.CharField(max_length=36L)
#     simname = models.CharField(max_length=255L)
#     posglobal = models.CharField(max_length=255L)
#     parcelname = models.CharField(max_length=255L)
#     classifiedflags = models.IntegerField()
#     priceforlisting = models.IntegerField()
#     class Meta:
#         db_table = 'classifieds'

# class Migrations(models.Model):
#     name = models.CharField(max_length=100L, blank=True)
#     version = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = 'migrations'

# class Userdata(models.Model):
#     userid = models.CharField(max_length=36L, db_column='UserId') # Field name made lowercase.
#     tagid = models.CharField(max_length=64L, db_column='TagId') # Field name made lowercase.
#     datakey = models.CharField(max_length=255L, db_column='DataKey', blank=True) # Field name made lowercase.
#     dataval = models.CharField(max_length=255L, db_column='DataVal', blank=True) # Field name made lowercase.
#     class Meta:
#         db_table = 'userdata'

# class Usernotes(models.Model):
#     useruuid = models.CharField(max_length=36L)
#     targetuuid = models.CharField(max_length=36L)
#     notes = models.TextField()
#     class Meta:
#         db_table = 'usernotes'

# class Userpicks(models.Model):
#     pickuuid = models.CharField(max_length=36L, primary_key=True)
#     creatoruuid = models.CharField(max_length=36L)
#     toppick = models.CharField(max_length=5L)
#     parceluuid = models.CharField(max_length=36L)
#     name = models.CharField(max_length=255L)
#     description = models.TextField()
#     snapshotuuid = models.CharField(max_length=36L)
#     user = models.CharField(max_length=255L)
#     originalname = models.CharField(max_length=255L)
#     simname = models.CharField(max_length=255L)
#     posglobal = models.CharField(max_length=255L)
#     sortorder = models.IntegerField()
#     enabled = models.CharField(max_length=5L)
#     class Meta:
#         db_table = 'userpicks'

class Interests(models.Model):
    """docstring for Interests"""
    interest = models.CharField(max_length=250)


class Userprofile(models.Model):
    user = models.ForeignKey(User)
    profilepartner = models.CharField(max_length=36, null=True, blank=True) # Field name made lowercase.
    profileallowpublish = models.BooleanField(default=False) # Field name made lowercase.
    profilematurepublish = models.CharField(max_length=1, null=True, blank=True) # Field name made lowercase.
    profileurl = models.CharField(max_length=255, null=True, blank=True) # Field name made lowercase.
    profilewanttomask = models.IntegerField(null=True, blank=True) # Field name made lowercase.
    profilewanttotext = models.CharField(max_length=250, null=True, blank=True) # Field name made lowercase.
    profileskillsmask = models.IntegerField(null=True, blank=True) # Field name made lowercase.
    profileskillstext = models.CharField(max_length=250, null=True, blank=True) # Field name made lowercase.
    profilelanguages = models.CharField(max_length=250, null=True, blank=True) # Field name made lowercase.
    profileimage = models.FileField(upload_to='images', null=True, blank=True) # This is for Real world profile picture
    profileabouttext = models.TextField(null=True, blank=True) # This is for Real world biography
    profilefirstimage = models.FileField(upload_to='images', null=True, blank=True) # This is for profile picture
    profilefirsttext = models.TextField(null=True, blank=True) # This is for biography.
    homepage = models.CharField(max_length=255, null=True, blank=True)
    displayname = models.CharField(max_length=50, null=True, blank=True)
    interest = models.ManyToManyField(Interests)

    def __unicode__(self):
        return "%s" % (self.displayname)
		