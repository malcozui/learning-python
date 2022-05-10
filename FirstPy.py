import math

# The "RunningTally(tm)" is from a Joe Marini Python Course for C# developers.
print("RunningTally(tm)")
print("Welcome to the tally keeper!")
run = True
total = 0
while run == True:
    try:
        str = input()
        if str == "quit":
            run = False
        else:
            val = int(str)
            total += val
            print(f"> {total}")
    except ValueError:
        pass

# Me messing with math stuff for python since Its something I'm comforable with already
def pi():
    d = 1
    sum = 0
    for i in range(0, 1000000):
        if i % 2 == 0:
            sum += 4/d
        else:
            sum -= 4/d
        d += 2
    return sum

print(f"Pi value is {pi()}")
print(math.e)
    