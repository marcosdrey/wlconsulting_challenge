from django.db import models
from django.contrib.auth.models import User


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="wallet", verbose_name="Usuário")
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, verbose_name="Saldo")

    class Meta:
        verbose_name = "Carteira"

    def __str__(self):
        return f"Carteira de {self.user.username}"


class Transaction(models.Model):
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sent_transactions",
        verbose_name="Remetente"
    )
    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="received_transactions",
        verbose_name="Destinatário"
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Quantia")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")

    class Meta:
        verbose_name = "Transferência"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Transferência de R${self.amount} de {self.sender.username} para {self.receiver.username}"
