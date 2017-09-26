from django.conf.urls import patterns, include, url
from views import account_summary

urlpatterns = patterns('',
	url(r'^accountsummery/$', 'account.views.account_summary', name='account_summary'),
	url(r'^changepassword/$', 'account.views.changepassword', name='change_password'),
	url(r'^contactinformation/$', 'account.views.contactinformation', name='contact_information'),
	url(r'^transactionhistory/$', 'account.views.transactionhistory', name='transaction_history'),
	url(r'^premiummembership/$', 'account.views.premium_membership', name='premium-membership'),
	url(r'^buy/$', 'account.views.buy', name='buy-linkin-dollar'),
	url(r'^account/(?P<buy_id>\w+)/placeorder/', 'account.views.palce_order', name='buy-place-order'),
)
