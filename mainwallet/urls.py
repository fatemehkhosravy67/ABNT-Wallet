from django.urls import path

from .views import BalanceViewSet, CreditViewSet, DebitViewSet

urlpatterns = [
    path('balance/', BalanceViewSet.as_view(), name='get_balance'),
    path('credit/', CreditViewSet.as_view(), name='get_credit'),
    path('debit/', DebitViewSet.as_view(), name='get_debit'),
]

