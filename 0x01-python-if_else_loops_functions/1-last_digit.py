#!/usr/bin/python3
import random

# This line should not change
number = random.randint(-10000, 10000)

# Get the last digit of the number, preserving the sign
if number < 0:
    last_digit = (abs(number) % 10) * -1
else:
    last_digit = abs(number) % 10
result = "Last digit of {} is {} and is".format(number, last_digit)

# Check conditions and append to result string
if last_digit > 5:
    result += " greater than 5"
elif last_digit == 0:
    result += " 0"
else:
    result += " less than 6 and not 0"

# Print the result
print(result)
