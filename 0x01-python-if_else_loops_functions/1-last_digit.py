#!/usr/bin/python3
import random

# This line should not change
number = random.randint(-10000, 10000)

# Get the last digit of the number
last_digit = number % 10
result = "last digit of {} is {}".format(number, last_digit)

# Check conditions and append to result string
if last_digit > 5:
    result += " and is greater than 5"
elif last_digit == 0:
    result += " and is 0"
else:
    result += " and is less than 6 and not 0"

# Print the result
print(result)
