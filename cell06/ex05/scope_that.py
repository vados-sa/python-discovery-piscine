#!/usr/bin/env python3

def add_one(x):
    try:
        return x + 1
    except TypeError:
        return "error"

global_var = 42

print(global_var)
print(add_one(global_var))



"""     
 - Changes made to variables within functions (local scope) 
don't directly affect variables in the global scope unless 
you explicitly reassign the result.
 - Python uses pass-by-value for function arguments, meaning a 
copy of the argument is passed to the function, not the original 
variable itself.
 """