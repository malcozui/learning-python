# My first attempt at making a library I've never done this in python lmao.
# import math

def factorial(fact):
    # multiplies the inputed number by all the numbers less than it up until 1
    retval = fact
    for i in range(fact, 2, -1):
        retval *= (i - 1)
    return retval

def concat_numbers(*args: int):
    retval = ""
    for arg in args:
        retval += str(arg)
    return retval


# catches if someone attepts to run this as a script instead of a lib.
if __name__ == "__main__":
    print("Dont run this file as a script!")