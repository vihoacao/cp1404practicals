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
    with open('guitars.csv', 'r') as file:
        for line in file:
            name, year, cost = line.strip().split(',')
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(guitars):
    print("Guitars:")
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")


def main():
    guitars = get_guitars()
    display_guitars(guitars)
    print("\nSorting guitars by year...")
    guitars.sort()
    display_guitars(guitars)


if __name__ == "__main__":
    main()
