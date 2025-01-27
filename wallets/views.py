from rest_framework.viewsets import ModelViewSet
from .models import Wallet, Transaction
from .serializers import WalletSerializer, TransactionSerializer


class UserWalletViewset(ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    http_method_names = ['get', 'put', 'patch', 'delete']


class TransactionViewset(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filterset_fields = {
        'created_at': ['gte', 'lte', 'exact'],
        'sender': ['exact'],
        'receiver': ['exact']
    }
