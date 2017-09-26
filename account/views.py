from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from grid_user.models import User
from models import Plan, UserPlan
from xlab.settings import LINKI_CURRENCY_RATE
from account.models import BuyLinki


@login_required
def account_summary(request):
    user = request.user
    userplan = UserPlan.objects.get(user=user)
    context = {}
    context['userplan'] = userplan
    return render(request, 'account/accont-summery.html', context)


def premium_membership(request):
    user = request.user
    userplan = UserPlan.objects.get(user=user)
    return render(request, 'account/premium-membership.html', {'userplan': userplan})


def changepassword(request):
    return render(request, 'account/change-password.html', {})


def contactinformation(request):
    return render(request, 'account/contact-information.html', {})


def transactionhistory(request):
    return render(request, 'account/transaction-history.html', {})


def buy(request):
    context = {'LINKI_CURRENCY_RATE': LINKI_CURRENCY_RATE}
    if request.POST:
        req = request.POST

        try:
            float(req.get('estimatedtotal'))
            float(req.get('transactionfee'))
            int(req.get('linkidollar'))
            float(req.get('usdollar'))
        except:
            context_err = context
            context_err['error'] = 'Please insert valid value'
            return render(request, 'account/my-funds.html', context_err)
        usdamount = format(float(req.get('usdollar')), '.2f')
        lnamount = req.get('linkidollar')
        txfees = req.get('transactionfee')

        buy = BuyLinki(usdamount=usdamount, lnamount=lnamount, txfees=txfees, user=request.user)
        buy.save()
        red = '/my/account/%s/placeorder/'%buy.id
        return HttpResponseRedirect(red)

    return render(request, 'account/my-funds.html', context)


def palce_order(request, buy_id):
    return render(request, 'account/buy-placeorder.html', {})
