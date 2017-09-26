from django.db import models
from grid_user.models import User


class Plan(models.Model):
    planname = models.CharField(max_length=255)
    plantype = models.CharField(max_length=255)
    rate = models.CharField(max_length=50)
    currency = models.CharField(max_length=50)

    def __unicode__(self):
        return '%s ** %s' % (self.planname, self.plantype)

    def billingtype(self):
        return '%s %s %s' % (self.currency, self.rate, self.plantype)


class UserPlan(models.Model):
    user = models.ForeignKey(User)
    plan = models.ForeignKey(Plan)
    nextbilling = models.DateField(null=True, blank=True)
    billingcountry = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.user.username

    def billingrate(self):
        if self.plan.plantype == 'free':
            return 'Free'
        else:
            return self.plan.billingtype

    def billingdate(self):
        if self.plan.plantype == 'free':
            return '--'
        else:
            return self.nextbilling

    def getmembership():
        pass

class BuyLinki(models.Model):
    user = models.ForeignKey(User)
    usdamount = models.CharField(max_length=50)
    lnamount = models.CharField(max_length=100)
    txfees = models.CharField(max_length=50)
    createdon = models.DateTimeField(auto_now_add=True)
