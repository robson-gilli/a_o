from stations import stations
from fares import fares
import card
import sys 

class Trip:
    def __init__(self):

        self.cost = 0.0
        self.origin = ''
        self.destination = ''

    def bus_trip(self, card):
        if (card.balance >= fares['bus_cost']):
            card.add_debit(fares['bus_cost'])
            self.cost = fares['bus_cost']
        else:
            raise ValueError("Balance is insuficient to take a bus trip")

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
        possible_fares = []
        for o in self.origin:
            for d in self.destination:
                possible_fares.append(self.get_possible_cost(o, d))
        return min(possible_fares)


    def get_possible_cost(self, origin_zone, destination_zone):
        cost = 0.0
        # Anywhere in Zone 1
        if (origin_zone == 1 and destination_zone == 1 ):
            cost = fares['cost_anywhere_zone_one']
        # Any one zone outside zone 1
        if (origin_zone != 1 and destination_zone != 1 and abs(origin_zone - destination_zone) == 0 ):
            cost = fares['cost_one_zone_outside_zone_one']
        # Any two zones including zone 1
        elif((origin_zone == 1 or destination_zone == 1) and abs(origin_zone - destination_zone) == 1 ):
            cost = fares['cost_two_zones_including_zone_one']
        # Any two zones excluding zone 1
        elif((origin_zone != 1 and destination_zone != 1) and abs(origin_zone - destination_zone) == 1 ):
            cost = fares['cost_two_zones_excluding_zone_one']
        # More than two zones (3+)
        elif(abs(origin_zone - destination_zone) > 1):
            cost = fares['more_than_two_zones']
        
        return cost

