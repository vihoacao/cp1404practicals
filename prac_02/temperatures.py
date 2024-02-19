"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def caculate_fahrenheit_to_celsius():
    global fahrenheit
    fahrenheit = celsius * 9.0 / 5 + 32


def caculate_celsius_to_fahrenheit():
    global celsius
    celsius = 5 / 9 * (fahrenheit - 32)


while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        caculate_fahrenheit_to_celsius()
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("fahrenheit: "))
        caculate_celsius_to_fahrenheit()
        print(f"Result: {celsius:.2f} F")

        # TODO: Write this section to convert F to C and display the result
        # Hint: celsius = 5 / 9 * (fahrenheit - 32)
        # Remove the "pass" statement when you are done. It's a placeholder.

    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")