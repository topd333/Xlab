from django.http import HttpResponse, HttpResponseRedirect
import json
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from string import letters, digits
import random
from random import choice
from django.conf import settings
from grid_user.forms import CreateUserForm
import xlab.settings
from models import TempUser, User
from slipstream.user.account import UserAccount
import logging
from django.shortcuts import render

log = logging.getLogger("[GRID_USER]: ")



def ajax_checkusername(request):
    datadict = {}
    username = request.POST.get('username', '')
    user = User.objects.filter(username=username)
    tempuser = TempUser.objects.filter(username=username)

    if user or tempuser:
        datadict['available'] = False
        datadict['username'] = username
    else:
        datadict['available'] = True
        datadict['username'] = username

    return HttpResponse(json.dumps(datadict), content_type="text/json")


def ajax_register_user(request):
    if not request.is_ajax():
        return HttpResponse(content="Invalid Request Method.", status=400)


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
            datadict = {'status': False}            
            datadict['err_message'] = 'Existing Account Of Same %s: Please register with different credentials'%xtest

            return HttpResponse(json.dumps(datadict), content_type="text/json")


        # Attempt to create a temporary user
        # try:
        #     tmp_user = TempUser.objects.create_temp_user(
        #         data['email'], data['firstname'], data['lastname'],
        #         key, data['password']
        #     )
        tmp_user =""
        try:
            tmp_user = form.save(commit=False)

            tmp_user.activation_key = key
            tmp_user.save()
            

        except:
            datadict = {'status': False}
            datadict['err_message'] = 'Existing Account: Please register with different credentials'
            return HttpResponse(json.dumps(datadict), content_type="text/json")

        # activate_link = '%s:%s'%(request.META['SERVER_NAME'], request.META['SERVER_PORT'])

        send_mail('Account activation link', 'Please use the link to activate your account: %s/activate?key=%s' %
                  (activation_server, key), from_address, [email])
        datadict = {'status': True}
        datadict['firstname'] = firstname
        datadict['lastname'] = lastname
        datadict['email'] = email
        datadict['id'] = tmp_user.id
        return HttpResponse(json.dumps(datadict), content_type="text/json")

    else:
        datadict = {'status': False, 'error': form.errors}
        return HttpResponse(
                    content=json.dumps(datadict),
                    mimetype='application/json'
                )


def ajax_accounttype_user(request):

    if request.method == 'POST':
        lastrid = request.POST['user_id']
        user = TempUser.objects.get(id=lastrid)
        user.accounttype = "basic membership"
        user.save()
        return HttpResponse(content_type="text/json", status=200)



def ajax_checkpassword(request):
    datadict = {}
    if not request.is_ajax():
        return HttpResponse(content="Invalid Request Method.", status=400)

    currentpass = request.POST.get('password', None)
    try:
        check = request.user.check_password(currentpass)
    except:
        check = False

    if check:
        datadict['status'] = True
    else:
        datadict['status'] = False
    

    return HttpResponse(json.dumps(datadict), content_type="text/json")