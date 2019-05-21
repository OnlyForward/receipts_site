from django.conf.urls import url

from .views import (
                    ReceiptAPIView,
                    # ReceipListSearchAPIView,
                    # ReceiptCreateAPIView,
                    # ReceiptDetailAPIView,
                    # ReceiptUpdateAPIView,
                    # ReceiptDeleteAPIView
                    )

urlpatterns = [
    url(r'^$',ReceiptAPIView.as_view()),
    # url(r'^create/$',ReceiptCreateAPIView.as_view()),
    # url(r'^(?P<id>\d+)/$',ReceiptDetailAPIView.as_view()),
    # url(r'^(?P<pk>\d+)/update/$', ReceiptUpdateAPIView.as_view()),
    # url(r'^(?P<pk>\d+)/delete/$', ReceiptDeleteAPIView.as_view()),
]