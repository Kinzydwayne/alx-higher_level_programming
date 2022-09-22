#!/usr/bin/python3
""""Print the alphabet in reverse order alternating upper- and lower-case."""
for i in range(0, 26):
    if i % 2 == 0:
        print("{:c}".format(122 - i), end="")
    else:
        print("{:c}".format(90 - i), end="")
