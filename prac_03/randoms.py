import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1? number 13
# What was the smallest number you could have seen, what was the largest?
# The smallest number could be 5, and the largest could be 20

# What did you see on line 2? number 7
# What was the smallest number you could have seen, what was the largest?
# The smallest number could be 3, and the largest could be 9
# Could line 2 have produced a 4? No, because the step is 2

# What did you see on line 3? a float number
# What was the smallest number you could have seen, what was the largest?
# The smallest number could be 2.5, and the largest could be 5.5

print(random.randint(1, 100))
