from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    (r'^transaction_history/$', 'grid_oxdata.views.transaction_history'),
    (r'^transferamount/$', 'grid_oxdata.views.transferamount'),
)
