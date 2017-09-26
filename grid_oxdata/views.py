from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from grid_oxdata.DbConnection import DjangoDbConnection
from grid_user.models import User, SyncUser
from django.utils import timezone


@login_required
def transaction_history(request):
    userid = request.user.principal_id
    db = DjangoDbConnection(dbname='oxdata')
    data = db.get_account_history(userid)
    amount = 0
    alldata = []
    for d in data:
        accountdict = {'date': '', 'detail': '', 'debit': '', 'credit': '', 'amount': ''}
        if int(d[2]) > 0:
            amount = amount + int(d[2])
            accountdict['detail'] = d[3]
            accountdict['credit'] = 'L$%s' % (int(d[2]))
            accountdict['amount'] = amount

        if int(d[2]) < 0:
            accountdict['detail'] = d[3]
            accountdict['debit'] = 'L$%s' % (int(d[2]))
            amount = amount + int(d[2])
            accountdict['amount'] = amount
        alldata.append(accountdict)
    context = {'amount': amount, 'accountdict': alldata, 'userid': userid}
    return render(request, "grid_oxdata/transaction_history.html", context)


def transferamount(request):
    users = User.objects.all()
    if request.POST:
        amount = request.POST.get('amount')
        touser = request.POST.get('toaccount')
        if not amount:
            return HttpResponseRedirect('/transaction/transferamount/')
        amount = int(amount)
        SourceAccount = touser
        DestinationAccount = request.user.principal_id
        description = '%s pays %s %s' %(request.user.get_firstname_lastname(), users.get(principal_id=touser).get_firstname_lastname(), amount)
        date = timezone.now().year
        IP = '0.0.0.0'
        query = " INSERT INTO  TransactionData (SourceAccount, SourceIP,\
         DestinationAccount, DestinationIP, TransactionAmount, TransactionDate,\
          Description)\
          VALUES('%s','%s','%s','%s','%s','%s','%s')\
           "%(SourceAccount, IP, DestinationAccount, IP, amount * -1, date, description)
        db = DjangoDbConnection(dbname='oxdata')
        db.insert_data(query)
        query = ''' INSERT INTO  TransactionData (SourceAccount, SourceIP,\
         DestinationAccount, DestinationIP, TransactionAmount, TransactionDate,\
           Description) \
          VALUES ('%s','%s','%s','%s','%s','%s','%s')\
          '''%(DestinationAccount, IP, SourceAccount, IP, amount, date, description)
        db.insert_data(query)
        db.commit_transaction()
    context = {'users': users}
    return render(request, "grid_oxdata/transferamount.html", context)



def discusresponse(request):

    return HttpResponse("Issue creating user account%s"%request)