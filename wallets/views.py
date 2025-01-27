from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Wallet
from .serializers import WalletSerializer


class UserWalletView(APIView):

    def get(self, request, *args, **kwargs):
        wallet = get_object_or_404(Wallet, user=request.user)
        serializer = WalletSerializer(wallet)
        return Response(serializer.data)
