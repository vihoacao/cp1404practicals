from prac_09.unreliable_car import UnreliableCar


def main():
    """Test the UnreliableCar class."""
    # Create a new unreliable car with name "Car 1", 100 units of fuel, and reliability of 50%
    my_car = UnreliableCar("Car 1", 100, 50)

    # Test driving the car for 30 km
    distance_driven = my_car.drive(30)
    if distance_driven == 0:
        print("The car failed to start.")
    else:
        print(f"The car drove {distance_driven} km.")


if __name__ == '__main__':
    main()
