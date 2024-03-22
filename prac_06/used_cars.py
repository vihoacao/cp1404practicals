"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car

limo = Car(100)
limo.add_fuel(20)
print(f"Fuel in the car: {limo.fuel}")
limo.drive(115)


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("My Car", 180)
    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(f"Fuel in limo: {limo.fuel}")
    limo.drive(115)
    print(my_car)
    print(limo)

main()
