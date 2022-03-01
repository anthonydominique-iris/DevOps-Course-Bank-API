import pytest
from bank_api.bank import Bank

class BankReport:
    def __init__(self, bank: Bank):
        self.bank2 = bank

def get_balance(self, name):
    account = self.bank2.get_account(name)
    return sum(total.amount for total in self._bank.transactions if total.account == account)


