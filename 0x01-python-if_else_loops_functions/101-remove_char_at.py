#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        # If n is out of bounds, return the original string
        return str

    # Create a copy of the string, omitting the character at index n
    result = ""
    for i in range(len(str)):
        if i != n:  # Skip the character at index n
            result += str[i]
    return result
