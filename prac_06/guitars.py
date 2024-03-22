from guitar import Guitar


def main():
    print("My guitars!")
    guitars = []
    guitar_number = 1
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:.2f} added.")
        guitar_number += 1

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, start=1):
        vintage_indicator = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar} {vintage_indicator}")


if __name__ == "__main__":
    main()
