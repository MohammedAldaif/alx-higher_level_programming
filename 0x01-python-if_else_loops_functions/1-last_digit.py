#!/usr/bin/python3
import random

# This line should not change
number = random.randint(-10000, 10000)

# Get the last digit of the number
num = abs(number) % 10
last_digit = num if number >= 0 else num * -1
result = "last digit of {} is {}".format(number, last_digit)

# Use match statement for pattern matching
match last_digit:
    case _ if last_digit > 5:
        result += " and is greater than 5"
    case 0:
        result += " and is 0"
    case _ if 0 < last_digit < 6:
        result += " and is less than 6 and not 0"

# Print the result
print(result)
