from django.db import models

# Create your models here.

class AuthList(models.Model):
  region_id = models.CharField(max_length=36)
  region_name = models.CharField(max_length=128)
  user_id = models.CharField(max_length=36)
  user_name = models.CharField(max_length=128)

  def __unicode__(self):
    return "%s - %s" % (self.region_name, self.user_name)
