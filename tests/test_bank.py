"""Unit tests for bank.py"""

from gettext import translation
from typing  import Set, List
from datetime import datetime

import pytest

from bank_api.bank import Bank, Account
"""from dataclasses import dataclass"""

@pytest.fixture
def bank() -> Bank:
    return Bank()


def test_accounts_are_immutable():
    account = Account('Immutable')
    with pytest.raises(Exception):
        # This operation should raise an exception
        account.name = 'Mutable'


def test_bank_creates_empty(bank: Bank):
    assert len(bank.accounts) == 0
    assert len(bank.transactions) == 0


def test_can_create_and_get_account(bank: Bank):
    bank.create_account('Test')
    account = bank.get_account('Test')

    assert len(bank.accounts) == 1
    assert account.name == 'Test'


def test_cannot_duplicate_accounts(bank: Bank):
    bank.create_account('duplicate')
    bank.create_account('duplicate')

    assert len(bank.accounts) == 1


def test_cannot_modify_accounts_set(bank: Bank):
    accounts = bank.accounts
    accounts.append(Account('New Account'))

    assert len(bank.accounts) == 0


# TODO: Add unit tests for bank.add_funds()
def test_add_funds(bank: Bank):   
    bank.create_account('Test')
    bank.add_funds('Test', 25)
    
    transactions = bank.transactions
    assert {t.amount for t in transactions} == {25}
    
def test_add_funds_isinteger(bank: Bank):
    """is the value an integer"""
    transactions = bank.transactions
    assert isinstance({t.amount for t in transactions} == {25}, int) == True

def test_add_funds_check_not_zero(bank: Bank):
    """trying to add zero"""
    transactions = bank.transactions
    assert {t.amount for t in transactions} < {1} 
    

