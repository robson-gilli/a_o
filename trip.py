from stations import stations
from fares import fares
import card

class Trip:
    def __init__(self):

        self.cost = 0.0
        self.origin = ''
        self.destination = ''

    def bus_journey(self, card):
        self.cost = fares['bus_cost']
        card.add_debit(fares['bus_cost'])

    def start(self, station, card):
        if (station in stations):
            if (card.balance >= fares['max_cost']):
                self.origin = stations[station]            
                self.cost = fares['max_cost']
                card.add_debit(fares['max_cost'])
            else:
                print('Balance is insuficient to enter the station')
        else:
            print("Invalid Station")

    def end(self, station, card):
        if (station in stations):
            self.destination = stations[station]
            self.cost = self.get_final_cost()
            card.add_credit(fares['max_cost'])
            card.add_debit(self.cost)
        else:
            print('This is awkward, but you are trying to exit from a station unknown to me.')

    def get_final_cost(self):
        trip_cost = 0
        trip_zones = self.get_trip_zones()

        if (len(trip_zones) == 1 and trip_zones[0] == 1):      # Anywhere in Zone 1
            trip_cost = fares['cost_anywhere_zone_one']
        elif (len(trip_zones) == 1 and trip_zones[0] != 1):    # Any one zone outside zone 1
            trip_cost = fares['cost_one_zone_outside_zone_one']
        elif (len(trip_zones) == 2 and 1 in trip_zones):    # Any two zones including zone 1
            trip_cost = fares['cost_two_zones_including_zone_one']
        elif (len(trip_zones) == 2 and 1 not in trip_zones):# Any two zones excluding zone 1
            trip_cost = fares['cost_two_zones_excluding_zone_one']
        elif (len(trip_zones) > 2):                         # More than two zones (3+)
            trip_cost = fares['more_than_two_zones']
        return trip_cost
            
    def get_trip_zones(self):
        o_set = set(self.origin)
        return list(o_set.intersection(self.destination))
