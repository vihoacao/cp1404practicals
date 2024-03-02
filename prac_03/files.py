name = input("Enter file name: ")

file = open("name.txt", "w")

file.write(name)

file.close()

# -----------------------------------------------------

file = open("name.txt", "r")

name = file.read()

print(f"Your name is {name}")

file.close()

# -----------------------------------------------------
file = open("numbers.txt", "r")

first_number = int(file.readline())
second_number = int(file.readline())
file.close()

result = first_number + second_number

print(result)

# -----------------------------------------------------
total = 0
file = open("numbers.txt", "r")

for line in file:
    total += int(line.strip())
print(total)