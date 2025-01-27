from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Wallet, Transaction


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'

    def validate_balance(self, value):
        if value < 0:
            raise serializers.ValidationError("O saldo não pode ser negativo.")
        return value


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    def validate(self, data):
        if data["sender"] == data["receiver"]:
            raise serializers.ValidationError("As contas de transferências devem ser diferentes")
        if data["amount"] < 0:
            raise serializers.ValidationError("O valor da transferência deve ser válido.")
        try:
            sender = data["sender"]
            if sender.wallet.balance < data["amount"]:
                raise serializers.ValidationError(f"Saldo insuficiente na conta de {sender.username}")
        except User.DoesNotExist:
            raise serializers.ValidationError(f"O usuário com o id {data["sender"]} não existe")
        return data
