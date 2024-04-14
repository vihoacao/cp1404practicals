from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    # Test the fare calculation for an 18 km trip with a fanciness of 4
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    hummer.drive(18)
    fare = hummer.get_fare()
    print(fare)
    assert fare == 48.78


main()
