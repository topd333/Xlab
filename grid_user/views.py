from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.contrib.auth import (
    authenticate, login, logout, REDIRECT_FIELD_NAME)
from django.conf import settings
from django.shortcuts import render_to_response, render
from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.http import is_safe_url
from string import letters, digits
import random
from random import choice
from django.contrib.auth.decorators import login_required
import xlab.settings
from models import TempUser, User
from slipstream.user.account import UserAccount
from grid_user.forms import CreateUserForm
import logging
log = logging.getLogger("[GRID_USER]: ")


def register_user(request):

    '''
      Provides the user registration

      Provide the user registration form in GET requests and processes the form on POST requests. 
    '''

    if request.POST:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            data = request.POST
            email = data['email']
            firstname = data['firstname']
            lastname = data['lastname']
            password = data['password']
            username = data['username']
            
            key = ''.join(choice(letters + digits) for i in range(64))

            log.info('Key Created: %s' % key)

            # Test for existing email / avatar name locally
            test = ''
            xtest = ''
            try:
                test = User.objects.get(firstname=firstname, lastname=lastname)
                xtest += "Firstname and Lastname exists"
            except ObjectDoesNotExist:
                pass

            try:
                test = User.objects.get(email=email)
                xtest += " Email exists"
            except ObjectDoesNotExist:
                pass

            try:
                test = User.objects.get(username=username)
                xtest += " Username exists"
            except ObjectDoesNotExist:
                pass

            x_user = UserAccount(
                data['firstname'],
                data['lastname'],
                data['password'],
                data['email'],
            )

            activation_server = settings.ACCOUNT_SERVER_ADDRESS
            account_server = settings.ACCOUNT_SERVER_URL
            from_address = settings.ACCOUNT_ADMIN_EMAIL

            # Test for existing user on grid


            if not x_user.test_account(account_server) or xtest != '':
            #if xtest != '':
                context = {}
                context['form'] = form
                context['err_message'] = 'Existing Account Of Same %s: Please register with different credentials'%xtest

                return render(request, "join_user.html", context)


            # Attempt to create a temporary user
            # try:
            #     tmp_user = TempUser.objects.create_temp_user(
            #         data['email'], data['firstname'], data['lastname'],
            #         key, data['password']
            #     )
            try:
                tmp_user = form.save(commit=False)
                tmp_user.activation_key = key
                tmp_user.save()

            except:
                context = {}
                context['form'] = form
                context['err_message'] = 'Existing Account: Please register with different credentials'
                return render(request, "join_user.html", context)

            # activate_link = '%s:%s'%(request.META['SERVER_NAME'], request.META['SERVER_PORT'])

            send_mail('Account activation link', 'Please use the link to activate your account: %s/activate?key=%s' %
                      (activation_server, key), from_address, [email])
            context = {}
            context['firstname'] = firstname
            context['lastname'] = lastname
            context['email'] = email
            return render(request, "grid_user/activate.html", context)

        else:
          
          context = {}
          context['form'] = form
    else:
        form = CreateUserForm()
        context = {}
        context['form'] = form
    
        #context['site_name'] = settings.SITE_NAME
        #context['page_title'] = 'Registration'
        #context['navbar'] = 'register_nav.html'

    return render(request, "join_user.html", context)


def activate_user(request):
    '''
      Provides the link for the account activation enail
    '''
    errors = ''

    if not request.GET.get('key', ''):
        errors.append('Missing "key"')
        response = HttpResponse("Error: %s" % errors)

    try:
        key = request.GET.get('key', '')
        t = TempUser.objects.get(activation_key=key)
    except ObjectDoesNotExist:
        return HttpResponse("No active registration for %s . Please re-register" % key)

    # Will create a real user here - grid first, then site
    x_user = UserAccount(
        t.firstname,
        t.lastname,
        t.password,
        t.email
    )
    account_server = settings.ACCOUNT_SERVER_URL
    if not x_user.create_account(account_server):
        return HttpResponse("Issue creating user account")


    user_id = x_user.UserId

    user = User.objects.create_user(
        t.email,
        t.firstname,
        t.lastname,
        user_id,
        t.username,
        t.dob,
        t.securtyq,
        t.securtya,
        t.avatarname,
        t.password
    )

    TempUser.objects.filter(activation_key=key).delete()

    pass_str = '****************'

    # return HttpResponse("First %s<br>Last %s<br>Email %s<br>Password
    # %s<br>Created %s<br>Key %s" % (t.firstname, t.lastname, t.email,
    # t.password, t.created, t.activation_key))
    # return HttpResponse("First %s<br>Last %s<br>Email %s<br>Password %s<br>Created %s<br>Key %s" 
    #     % (t.firstname, t.lastname, t.email, pass_str, t.created, t.activation_key))
    context = {'username': t.username}
    if t.avatarname:
        avatarurl = '/'.join(t.avatarname.split('-'))
        context['avatarurl'] = avatarurl
    
    
    return render(request, "grid_user/activate.html", context)


def login_user(request, template_name='gridauth.html',
               redirect_field_name=REDIRECT_FIELD_NAME):
    """
    Login the user
    """
    log.info("Hey There")
    
    redirect_to = request.REQUEST.get(redirect_field_name, '')
    # This will go away...
    state = ""
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/')

    email = password = ''
    form_action = "/login/"
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')
        log.info("About to authenticate")
        log.info("email: %s, password: %s"% (email, password)) 
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "Login success"
                log.info("Login success")

                if not redirect_to:
                    redirect_to = "/"

                if not is_safe_url(url=redirect_to, host=request.get_host()):
                    # Will put them back on "/"
                    redirect_to = "/"

                return HttpResponseRedirect(redirect_to)

            else:
                state = "Your account is not active, please contact the site admin."

        else:
            state = "Your username and/or password were incorrect."

        #return HttpResponse(state)
        context = {}
        context['form_action'] = form_action
        context['state'] = state
        return render(request, 'index.html', context)

    else:
        if redirect_to:
            form_action = '/login/' + '?next=' + redirect_to

        context = {}
        context['navbar'] = 'site_nav.html'
        context['site_name'] = settings.SITE_NAME
        context['page_title'] = 'Login'
        context['email'] = email
        context['form_action'] = form_action
        context['redirect_field_name'] = redirect_to
        context['state'] = state

        return render(request, 'index.html', context)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")


# *************[ User Account Management ]*************************************
@login_required
def user_password(request):
    return HttpResponse("Manage Password")



# *************[ User Web Profiles ]*******************************************
def user_web_profiles(request):
    reply = ""

    for k, v in request:
        reply += "Key %s -- Val %s" % (k, v)

    return HttpResponse("Hello")


def join_user(request):
    context = {'a': 'a'}
    return render(request, 'join_user.html', context)


def completed(request):
    return HttpResponse("Manage Password")
