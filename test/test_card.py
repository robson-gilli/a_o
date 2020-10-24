import pytest
from ..src.card import Card

def test_card_add_credit():
    c = Card()
    c.add_credit(30.0)
    assert c.balance == 30.0

def test_card_add_credit_not_float():
    with pytest.raises(ValueError):
        c = Card()
        assert c.add_credit(30)

def test_card_add_debit():
        c = Card()
        c.add_credit(30.0)
        c.add_debit(10.0)
        assert c.balance == 20

def test_card_add_debit_not_float():
    with pytest.raises(ValueError):
        c = Card()
        c.add_credit(30.0)
        assert c.add_debit(10)

def test_card_add_debit_not_enough_balance():
    with pytest.raises(ValueError) as excinfo:
        c = Card()
        c.add_debit(10.0)
    assert "Not enough credit!" in str(excinfo.value)
