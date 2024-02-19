password = input("Enter your password: ")

while len(password) < 8:
    print("Password must be at least 8 characters")
    password = input("Enter your password: ")

print("*" * len(password))