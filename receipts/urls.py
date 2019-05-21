from django.conf.urls import url, include
from django.contrib import admin
from receipts.views import *

app_name = 'receipts'

urlpatterns = [
    url(r'create_receipt/$', ReceiptsCreate.as_view(), name='create_receipt'),
    url('signup/$', sign_up_page, name='signUp'),
    url('signIn/$', sign_in_page, name='signIn'),
    url('blogs/$', blogs_page, name='blogs'),
    url(r'^(?P<pk>\d+)/$', ReceiptsDetailView.as_view(), name='detail'),
    url(r'^update/(?P<pk>\d+)/$', ReceiptsUpdate.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', ReceiptsDelete.as_view(), name='delete'),
    url(r'^list/$', ReceiptsListView.as_view(), name='list'),

]
