import random
import datetime
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils import timezone

SECURTYQUESTION = (
    ('1', "What city were you born in?"),
    ('2', "What is your mother's maiden name?"),
    ('3', "What street did you grow up on?"),
    ('4', "What is the title of your favorite book?"),
    ('5', "What is your favorite vacation spot?"),
    ('6', "What is your pet's name?"),
)


class UserManager(BaseUserManager):

    def create_user(self, email, first, last, principal, username, dob, securtyq,
                    securtya, avatarname, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        if not principal:
            raise ValueError('Users must have a principal id')

        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=UserManager.normalize_email(email),
            firstname=first,
            lastname=last,
            principal_id=principal,
            username=username,
            securtyq=securtyq,
            securtya=securtya,
            dob=dob,
            avatarname=avatarname
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, firstname, lastname, principal_id, password):
        """
        Creates and saves a superuser with the given parameters
        """
        # securtyq = '1'
        # securtya = 'india'
        # dob = '2014-08-18'#datetime.date.today
        # avatarname = 'people-pic1.png'

        # user = self.create_user(email,
        #     firstname, lastname, principal_id, username, dob, securtyq, securtya, avatarname, password,
        # )
        user = self.model(
            username=username,
            email=UserManager.normalize_email(email),
            firstname=firstname,
            lastname=lastname,
            principal_id=principal_id
        )
        user.set_password(password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        db_index=True,
    )
    username = models.CharField(max_length=255, unique=True)
    dob = models.DateField(default=datetime.date.today)

    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    principal_id = models.CharField(max_length=36)
    scope_id = models.CharField(
        max_length=36,
        default='00000000-0000-0000-0000-000000000000'
    )
    securtyq = models.CharField(
        max_length=255, choices=SECURTYQUESTION, default='1')
    securtya = models.CharField(max_length=255, default='india')

    user_level = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    avatarname = models.CharField(max_length=250, blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'firstname', 'lastname', 'principal_id']

    def get_full_name(self):
        self.email

    def get_short_name(self):
        self.email

    def __unicode__(self):
        return '%s ** %s %s' % (self.email, self.firstname, self.lastname)

    def has_perms(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def get_firstname_lastname(self):
        return '%s %s' % (self.firstname, self.lastname)

    # @property
    # def is_staff(self):
    #   "Is the user a member of staff?"
    # Simplest possible answer: All admins are staff
    #   return self.is_admin


class TempUserManager(models.Manager):

    def create_temp_user(self, email, firstname, lastname, key, username, dob, securtyq, securtya, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        temp_user = self.model(
            email=UserManager.normalize_email(email),
            username=username,
            firstname=firstname,
            lastname=lastname,
            securtyq=securtyq,
            securtya=securtya,
            activation_key=key,
            password=password
        )
        temp_user.save(using=self._db)
        return temp_user


class TempUser(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=95, unique=True)
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    password = models.CharField(max_length=20)
    dob = models.DateField()
    securtyq = models.CharField(max_length=255, choices=SECURTYQUESTION)
    securtya = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now=True)
    activation_key = models.CharField(max_length=64)
    avatarname = models.CharField(max_length=250, blank=True, null=True)
    accounttype = models.CharField(
        max_length=64, blank=True, default='basic membership')

    objects = TempUserManager()

    def __unicode__(self):
        return '%s ** %s %s ** %s' % (self.email,
                                      self.firstname,
                                      self.lastname,
                                      self.created)


class ChangeEmailManager(models.Manager):

    def create_temp_email(self, email, key):

        if not email:
            raise ValueError('Users must have an email address')

        temp_email = self.model(
            email=ChangeEmailManager.normalize_email(email),
            activation_key=key
        )
        temp_email.save(using=self._db)
        return temp_email


class ChangeEmail(models.Model):

    email = models.EmailField(max_length=95, unique=True)
    created = models.DateTimeField(auto_now=True)
    activation_key = models.CharField(max_length=64)


class ChangePasswordManager(models.Manager):

    def create_confirmation(self, password, key, cuser_id):

        temp_password = self.model(
            password=password,
            activation_key=key,
            user_id=cuser_id,
        )
        temp_password.save(using=self._db)
        return temp_password


class ChangePassword(models.Model):

    password = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now=True)
    activation_key = models.CharField(max_length=64)
    user_id = models.CharField(max_length=50, blank=True, null=True)
    objects = ChangePasswordManager()


class SyncUser(models.Model):

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        db_index=True,
    )
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    principal_id = models.CharField(max_length=36)
    scope_id = models.CharField(
        max_length=36,
        default='00000000-0000-0000-0000-000000000000'
    )

    user_level = models.IntegerField(default=0)

    def __unicode__(self):
        return '%s ** %s %s' % (self.firstname,
                                self.lastname,
                                self.email)
