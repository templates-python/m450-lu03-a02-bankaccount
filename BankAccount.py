from dataclasses import dataclass


@dataclass
class BankAccount:
    """
    a bank account
    """
    Balance: float

    def get_money(self, value):
        if value < self.Balance:
            self.Balance -= value
            return value
        else:
            return 0

    @property
    def Balance(self):
        return self._balance

    @Balance.setter
    def balance(self, value):
        self._balance = value
