#!/usr/bin/env python3

def greetings(name = 'noble stranger'):
    if isinstance(name, str) == True:
        print(f"Hello, {name}.")
    else:
        print("Error! It was not a name")

greetings('Alexandra')
greetings('Vanessa')
greetings('Wil')
greetings()
greetings(42)