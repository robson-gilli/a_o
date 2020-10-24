from stations import stations
from fares import fares
import card
import sys 

class Trip:
    def __init__(self):

        self.cost = 0.0
        self.origin = ''
        self.destination = ''

    def bus_journey(self, card):
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
        trip_cost = 0
        trip_zones = self.get_trip_zones(self.origin, self.destination)
        zone_one_crossed = self.trip_include_zone_one(self.origin, self.destination)
        # Anywhere in Zone 1
        if (trip_zones == 1 and zone_one_crossed):      
            trip_cost = fares['cost_anywhere_zone_one']
        # Any one zone outside zone 1
        elif (trip_zones == 1 and not zone_one_crossed):    
            trip_cost = fares['cost_one_zone_outside_zone_one']
        # Any two zones including zone 1
        elif (trip_zones == 2 and zone_one_crossed):        
            trip_cost = fares['cost_two_zones_including_zone_one']
        # Any two zones excluding zone 1
        elif (trip_zones == 2 and not zone_one_crossed):    
            trip_cost = fares['cost_two_zones_excluding_zone_one']
        # More than two zones (3+)
        elif (trip_zones > 2):                             
            trip_cost = fares['more_than_two_zones']
        return trip_cost

    def get_trip_zones(self, origin, destination):
        zones_visited = sys.maxint
        for o in origin:
            for d in destination:
                if (abs(o - d) + 1 < zones_visited):
                    zones_visited = abs(o - d) + 1

        return zones_visited

    def trip_include_zone_one(self, origin, destination):
        return ((len(origin) == 1 and 1 in origin) or ((len(destination) == 1 and 1 in destination)))