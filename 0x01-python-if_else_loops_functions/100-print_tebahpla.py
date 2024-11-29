#!/usr/bin/python3
def print_tebahpla():
    i = 122
    while i >= 97:
        print("{}".format(chr(i) if i % 2 == 0 else chr(i-32)), end='')
        i = i - 1


print_tebahpla()
