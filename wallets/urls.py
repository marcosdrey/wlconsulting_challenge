from django.urls import path
from . import views

urlpatterns = [
    path("wallet/", views.UserWalletView.as_view(), name="user_wallet")
]
