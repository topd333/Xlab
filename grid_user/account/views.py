from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.context_processors import csrf
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render_to_response, render
from django.template import loader,RequestContext
import xlab.settings
from django.contrib.auth.decorators import login_required
from slipstream.user.account import UserAccount
import logging
from string import letters, digits
import random
from random import choice

from grid_user.models import ChangeEmail, ChangePassword, User

log = logging.getLogger("[GRID_USER]: ")

@login_required
def user(request):
  
  context = {} 
  context['SiteName'] = settings.SITE_NAME
  context['SiteTitle'] = 'Account'
  context['navbar'] = 'account_nav.html'
  context['application'] = 'summary' #start with a summary

  return render(request, "account.html", context)

@login_required
def change_password(request):
  account_server = settings.ACCOUNT_SERVER_URL
  #account_server = "http://127.0.0.1:8000"
  from_address = settings.ACCOUNT_ADMIN_EMAIL

  if request.POST:
    data = request.POST

    password = data.get('pass', None)
    key = ''.join(choice(letters + digits) for i in range(64))
    cuser_id = request.user.id
    pwc = ChangePassword.objects.create_confirmation(password, key, cuser_id)


    email = request.user.email

    activate_link = '%s:%s' %(request.META['SERVER_NAME'], request.META['SERVER_PORT'])
    send_mail('Xlab Account: Password change confirmation link', 'Please use the link to confirm the password change on your account: %s/account/change_password?key=%s'%(account_server, key), from_address, [email])
    
    
    
    context = {}
    context['SiteName'] = settings.SITE_NAME
    context['SiteTitle'] = 'Xlab'
    context['navbar'] = 'account_nav.html'
    context['application'] = 'summary'
    context['notify'] = 'Confirmation link has been sent to your registered email address'

    return render(request, "account/change-password.html", context)
  
  else:
    errors = []
    if not request.GET.get('key', ''):
      errors.append('Missing "key"')
      response = HttpResponse("Error: %s"% errors)

    
    try:
      key = request.GET.get('key', '')
      cuser_id = request.GET.get('')
      passwd = ChangePassword.objects.get(activation_key=key)
      user = User.objects.get(id=passwd.user_id)
      user.set_password(passwd.password)
      user.save()
     

      

    except:
      return HttpResponse("No active task for %s. Please try again" % key)

    return HttpResponse("Hey %s" % key)
   

@login_required
def change_email(request):
  # Create temporary object as in temp user
  # User will follow the link to get the change on the reqested address
  pass



