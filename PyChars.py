# All chars

def main():
    #prints out all the unicode characters up to 2 ^ (whatever you input.)
    exp = int(input("Please input the exponent you'd like => "))
    exp -= 1
    print(f"your exponent will generate {((2**exp) - 16) if (((2**exp) - 16) >= 0) else (0) } terms.")
    for i in range(15, 2**exp, 1):
        if i > 55295: # 55295 is currently the highest magnitute char convertable by python.
            break
        print(f"i: {str(i)}. chr: {chr(i)}", sep="=", end=" ")
        if i % 10 == 0:
            print(" => ", end="\n")

#running as a script versus library check.
if __name__ == "__main__":
    main()