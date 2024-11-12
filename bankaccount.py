from dataclasses import dataclass


@dataclass
class BankAccount:
    """
    a bank account
    """
    balance: float

    def get_money(self, value):
        if value < self.balance:
            self.balance -= value
            return value
        else:
            return 0

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
