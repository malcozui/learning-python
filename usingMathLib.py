#using the library i made
import mathLibpy

# expected output 120
print(mathLibpy.factorial(5))
# status update it worked! 

# expected output 123
print(f"1 + 2 + 3 maybe is {mathLibpy.concat_numbers( 1, 2, 3 )}")
# status update it works!

# expected output 6
print(f"ok but really 1 + 2 + 3 is {mathLibpy.sum( 1, 2, 3)}")
# status update it works

# expected output 2.718 etc
print(f"e is {mathLibpy.exp(1)}")
# status update it works