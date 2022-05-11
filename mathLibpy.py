# My first attempt at making a library I've never done this in python lmao.
import math as m

def factorial(fact: int):
    # multiplies the inputed number by all the numbers less than it up until 1
    if fact == 0 | fact == 1:
        return 1
    retval = fact
    for i in range(fact, 2, -1):
        retval *= (i - 1)
    return retval

def sum(*args):
    retval = 0
    for arg in args:
        retval += arg
    return retval

def concat_numbers(*args: int):
    retval = ""
    for arg in args:
        retval += str(arg)
    return retval

def exp(num: int):
    retval = 1
    for i in range(1, 100):
        retval += (num ** i) / factorial(i)
    return retval

def natural_log(num: int):
    # I'm cheating here since IDK the taylor expansion fror the natual log
    retval = m.log(num)
    return retval


# catches if someone attepts to run this as a script instead of a lib.
if __name__ == "__main__":
    print("Dont run this file as a script!")