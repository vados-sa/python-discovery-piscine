#!/usr/bin/env python3

import sys

#takes a string as a parameter and displays the first eight
#characters of that string.
def shrink(str):
    print(str[0:8])

#takes a string as a parameter and appends ’Z’ characters to
#make it a total of eight characters.
def enlarge(str):
    l = len(str)
    i = 8 - l
    while i > 0:
        str = str + "Z"
        i -= 1
    print(str)

if len(sys.argv) < 2:
    print("none")

else:
    for str in sys.argv[1:]:
        if len(str) > 8:
            shrink(str)
        elif len(str) < 8:
            enlarge(str)
        else:
            print(str) 