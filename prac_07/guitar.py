class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def __lt__(self, other):
        return self.year < other.year


def get_guitars():
    guitars = []
    try:
        with open('guitars.csv', 'r') as file:
            for line in file:
                name, year, cost = line.strip().split(',')
                guitars.append(Guitar(name, int(year), float(cost)))
    except FileNotFoundError:
        print("No existing data file found. Starting with an empty list.")
    return guitars


def add_guitar():
    name = input("Enter the name of the guitar: ")
    year = int(input("Enter the year of the guitar: "))
    cost = float(input("Enter the cost of the guitar: "))
    return Guitar(name, year, cost)


def display_guitars(guitars):
    print("Guitars:")
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")


def write_guitars(guitars):
    with open('guitars.csv', 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


def main():
    guitars = get_guitars()
    display_guitars(guitars)

    add_more = input("Do you want to add more guitars? (yes/no): ").lower()
    while add_more == "yes":
        guitars.append(add_guitar())
        add_more = input("Do you want to add more guitars? (yes/no): ").lower()

    write_guitars(guitars)


if __name__ == "__main__":
    main()
