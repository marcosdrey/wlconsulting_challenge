from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register("wallets", views.UserWalletViewset, basename="wallet")
router.register("transactions", views.TransactionViewset, basename="transaction")

urlpatterns = [
    path("", include(router.urls)),
]
