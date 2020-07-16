# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
# start 2:10 EST 7/16/2020

class Vehicle: # base class
    pass

class FlightVehicle(Vehicle): # Flight is subclass of base Vehicle
    pass

class GroundVehicle(Vehicle): # Ground is subclass of base Vehicle
    pass

class Car(GroundVehicle): # Car is subclass of base GroundVehicle which is a sub of Vehicle base class
    pass

class Motorcycle(GroundVehicle): # Motorcycle is subclass of base GroundVehicle which is a sub of Vehicle base class
    pass

class Airplane(FlightVehicle): # Airplane is subclass of base FlightVehicle which is a sub of Vehicle base class
    pass

class Starship(FlightVehicle): # Starship is subclass of base FlightVehicle which is a sub of Vehicle base class
    pass