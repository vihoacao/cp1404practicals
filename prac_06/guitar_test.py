from guitar import Guitar


def test_guitar():
    gibson_l5_ces = Guitar("Gibson L-5 CES", 1922, 16035.40)

    # Test get_age method
    print(f"{gibson_l5_ces.name} get_age() - Expected 100. Got {gibson_l5_ces.get_age(2022)}")
    # Test is_vintage method
    print(f"{gibson_l5_ces.name} is_vintage() - Expected True. Got {gibson_l5_ces.is_vintage(2022)}")

    another_guitar = Guitar("Another Guitar", 2013)
    print(f"{another_guitar.name} get_age() - Expected 9. Got {another_guitar.get_age(2022)}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage(2022)}")


if __name__ == "__main__":
    test_guitar()
