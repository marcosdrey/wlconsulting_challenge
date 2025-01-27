import random
from decimal import Decimal
from django.core.management import BaseCommand
from django.contrib.auth.models import User
from wallets.models import Transaction


class Command(BaseCommand):
    def handle(self, *args, **options):
        QT_USERS_TO_BE_CREATED = 10
        QT_TRANSACTIONS_TO_BE_CREATED = 50

        self.stdout.write(
            self.style.NOTICE("Criando usuários...")
        )
        for n in range(QT_USERS_TO_BE_CREATED):
            self.__create_user_and_add_wallet_balance(n)

        self.stdout.write(
            self.style.NOTICE("Criando transferências...")
        )
        for n in range(QT_TRANSACTIONS_TO_BE_CREATED):
            sender = self.__get_random_user()
            receiver = self.__get_random_user()
            while sender.id == receiver.id:
                receiver = self.__get_random_user()
            Transaction.objects.create(
                sender=sender,
                receiver=receiver,
                amount=sender.wallet.balance / 2
            )

        self.stdout.write(
            self.style.SUCCESS("Usuários, carteiras e transferências criados com sucesso!")
        )

    @staticmethod
    def __create_user_and_add_wallet_balance(n):
        username = f"teste{n}"
        password = f"teste{n}_senha"
        new_user = User.objects.create(username=username, password=password)

        decimal_value = Decimal(str(float(random.randint(100, 1000))))
        wallet = new_user.wallet
        wallet.balance = decimal_value
        wallet.save()

    @staticmethod
    def __get_random_user():
        return User.objects.order_by("?").first()
