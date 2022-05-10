#more code from the Joe Marini Python course
#Functions

def myfunc():
    print("returning 42")
    return 42

def myvoidfunc(x, y):
    print("returning nothing")
    print(x + y)

def myvariableargs(a, b, *args):
    print(a + b)
    for arg in args:
        print(arg)

retval = myfunc()
print (retval)

retval = myvoidfunc(5, 10)
# pythons equivenlent of a turnary operator.
print(retval) if retval is not None else print("Nah couldnt do it")

myvariableargs(1, 2, "bob", 3.45, "23")