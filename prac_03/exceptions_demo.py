"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? when user enter invalid numerator and denominator.
2. When will a ZeroDivisionError occur? when the denominator equal 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

valid_input = False
while not valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        if denominator == 0:
            print("The denominator is invalid!")
            # denominator = int(input("Enter the denominator: "))
        else:
            fraction = numerator / denominator
            print(fraction)
            valid_input = True
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
print("Finished.")

# ValueError occur when we enter somthing that are not integers
# ZeroDivisionError occur when we enter 0 as denominator
