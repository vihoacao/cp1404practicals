def main():
    password = get_password()
    print_the_asterisks(password)


def get_password():
    password = input("Enter your password: ")
    while len(password) < 8:
        print("Password must be at least 8 characters")
        password = input("Enter your password: ")
    return password


def print_the_asterisks(password):
    print("*" * len(password))


main()
