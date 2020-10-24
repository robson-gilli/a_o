# -*- coding: utf-8 -*-
from card import Card
from trip import Trip
from stations import stations

c = Card()
print("=========================================================")
print("Adding 30 to balance")
c.add_credit(30.0)
print("Card balance is: " + str(c.balance))
print("=========================================================\n")

print("\n=========================================================")
print("Starting Tube trip from Holborn to Earl’s Court")
t1 = Trip()
t1.start('Holborn', c)
t1.end('EarlsCourt', c)
print("Tube trip from Holborn to Earl’s Court ended. Trip cost = " + str(t1.cost))
print("Your card balance is " + str(c.balance))

print("\n=========================================================")
print("Starting Trip 328 bus from Earl’s Court to Chelsea")
t2 = Trip()
t2.bus_journey(c)
print("Trip 328 bus from Earl’s Court to Chelsea. Trip cost = " + str(t2.cost))
print("Your card balance is " + str(c.balance))

print("\n=========================================================")
print("Starting Tube trip from Earl’s court to Hammersmith")
t3 = Trip()
t3.start('EarlsCourt', c)
t3.end('Hammersmith', c)
print("Tube trip from Earl’s court to Hammersmith. Trip cost = " + str(t3.cost))
print("Your card balance is " + str(c.balance))
print("=========================================================")

