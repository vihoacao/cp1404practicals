# display menu
# get choice
# while choice != <quit option>
#     if choice == <first option>
#         <do first task>
#     else if choice == <second option>
#         <do second task>
#     ...
#     else if choice == <n-th option>
#         <do n-th task>
#     else
#         display invalid input error message
#     display menu
#     get choice
# <do final thing, if needed>

MENU = """
G - Enter a valid score (must be 0-100)
P - Print result
S - Show stars
Q - Quit
"""
print(MENU)
choice = input(">>>").upper()
score = 0


def get_score():
    global score
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score!")
        score = int(input("Enter score: "))


def get_result():
    global score
    if score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_result(score, result):
    print(f"Score: {score}, Result: {result}")


def show_stars(score):
    print("*" * score)


while choice != "Q":
    if choice == "G":
        get_score()
    elif choice == "P":
        result = get_result()
        print_result(score, result)
    elif choice == "S":
        show_stars(score)
    else:
        print("Invalid option!")
    print(MENU)
    choice = input(">>> ").upper()

print("Farewell.")
