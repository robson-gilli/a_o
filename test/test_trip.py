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
        
def test_trip_get_trip_zones_one_zone():
        c = Card()
        c.add_credit(3.2)

        t = Trip()
        ret = t.get_trip_zones([2],[2])
        assert ret == 1

def test_trip_get_trip_zones_two_zone():
        c = Card()
        c.add_credit(3.2)

        t = Trip()
        ret = t.get_trip_zones([2],[1])
        assert ret == 2

def test_trip_get_trip_zones_three_zone():
        c = Card()
        c.add_credit(3.2)

        t = Trip()
        ret = t.get_trip_zones([3],[1])
        assert ret == 3

def test_trip_get_trip_zones_one_zone_intersection():
        c = Card()
        c.add_credit(3.2)

        t = Trip()
        ret = t.get_trip_zones([2],[1,2])
        assert ret == 1

def test_trip_trip_include_zone_one_true():
        c = Card()
        c.add_credit(3.2)

        t = Trip()
        ret = t.trip_include_zone_one([1],[1,2])
        assert ret == True

def test_trip_trip_include_zone_one_false():
        c = Card()
        c.add_credit(3.2)

        t = Trip()
        ret = t.trip_include_zone_one([1,2],[1,2])
        assert ret == False

        ret = t.trip_include_zone_one([2],[3])
        assert ret == False

        ret = t.trip_include_zone_one([2],[2])
        assert ret == False

        ret = t.trip_include_zone_one([2,3],[2])
        assert ret == False
