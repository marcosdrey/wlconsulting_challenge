from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Wallet, Transaction


@receiver(post_save, sender=User)
def create_wallet_for_new_user(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(user=instance)


@receiver(post_save, sender=Transaction)
def manage_transaction_value(sender, instance, created, **kwargs):
    if created and instance.sender.wallet.balance >= instance.amount:
        sender_user_wallet = instance.sender.wallet
        sender_user_wallet.balance -= instance.amount
        sender_user_wallet.save()

        receiver_user_wallet = instance.receiver.wallet
        receiver_user_wallet.balance += instance.amount
        receiver_user_wallet.save()
