import csv


def read_csv_file(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        return list(reader)


def count_champions(data):
    champions = {}
    for row in data:
        name = row[2]
        if name in champions:
            champions[name] += 1
        else:
            champions[name] = 1
    return champions


def get_countries(data):
    countries = set()
    for row in data:
        countries.add(row[1])
    return sorted(countries)


def display_champions(champions):
    print("Wimbledon Champions:")
    for champion, count in champions.items():
        print(f"{champion} {count}")


def display_countries(countries):
    print("\nThese countries have won Wimbledon:")
    print(", ".join(countries))


def main():
    filename = "wimbledon.csv"
    data = read_csv_file(filename)
    champions = count_champions(data)
    countries = get_countries(data)
    display_champions(champions)
    display_countries(countries)


if __name__ == "__main__":
    main()
