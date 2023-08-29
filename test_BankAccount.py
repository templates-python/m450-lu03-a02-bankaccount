from BankAccount import BankAccount


def test_get_money_less_than_saldo_returns_expected_money():
    account = BankAccount(400)
    value = account.get_money(300)
    assert value == 300 and account.balance == 100


def test_get_money_with_more_than_saldo_returns_nothing():
    account = BankAccount(400)
    value = account.get_money(600)
    assert value == 0 and account.balance == 400