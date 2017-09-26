from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from models import User, TempUser, SyncUser

admin.site.register(User)
admin.site.register(TempUser)
admin.site.register(SyncUser)
