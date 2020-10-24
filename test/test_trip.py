import pytest
from ..src.card import Card
from ..src.trip import Trip

def test_trip_bus_trip():
    c = Card()
    c.add_credit(1.8)

    t = Trip()
    t.bus_journey(c)

    assert c.balance == 0.0

def test_trip_bus_trip_not_enough_balance():
    with pytest.raises(ValueError) as excinfo:
        c = Card()
        c.add_credit(1.0)

        t = Trip()
        t.bus_journey(c)
    assert "Balance is insuficient to take a bus trip" in str(excinfo.value)

    
def test_trip_tube_zone1():
        c = Card()
        c.add_credit(3.2)

        t = Trip()
        t.start('Holborn', c)
        t.end('EarlsCourt', c)

        assert round(c.balance, 2) == 0.7

def test_trip_tube_one_zone_not_zone1():
        c = Card()
        c.add_credit(3.2)

        t = Trip()
        t.start('Hammersmith', c)
        t.end('EarlsCourt', c)

        assert round(c.balance, 2) == 1.2

def test_trip_tube_two_zones_include_zone1():
        c = Card()
        c.add_credit(3.2)

        t = Trip()
        t.start('Holborn', c)
        t.end('Hammersmith', c)

        assert round(c.balance, 2) == 0.2

def test_trip_tube_two_zones_exclude_zone1():
        c = Card()
        c.add_credit(3.2)

        t = Trip()
        t.start('Wimbledon', c)
        t.end('Hammersmith', c)

        assert round(c.balance, 2) == 0.95


def test_trip_tube_more_than_two_zones():
        c = Card()
        c.add_credit(3.2)

        t = Trip()
        t.start('Wimbledon', c)
        t.end('Holborn', c)

        assert round(c.balance, 2) == 0.0
        
def test_trip_get_possible_cost():
    t = Trip()

    cost = t.get_possible_cost(1, 1)
    assert cost == 2.5

    cost = t.get_possible_cost(2, 2)
    assert cost == 2.0

    cost = t.get_possible_cost(1, 2)
    assert cost == 3.0

    cost = t.get_possible_cost(3, 2)
    assert cost == 2.25

    cost = t.get_possible_cost(3, 1)
    assert cost == 3.2
