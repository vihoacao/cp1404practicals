"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


# TODO: Fix this!


def main():
    score = float(input("Enter score: "))
    result = get_result(score)
    print_result(score, result)


def get_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_result(score, result):
    print(f"Score: {score:.2f}, Result: {result}")


main()
