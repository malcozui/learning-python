import time
import random
from DirectInputLib import PressKey, ReleaseKey, W, A, S, D

dirs = [ W, A, S, D]

def SingleMove():
    dir = random.randint(0,(len(dirs) - 1))
    PressKey(dirs[dir])
    time.sleep(random.randint(1, 5))
    ReleaseKey(dirs[dir])

def DoubleMove():
    dir1 = random.randint(0,(len(dirs) - 1))
    dir2 = random.randint(0,(len(dirs) - 1))
    PressKey(dirs[dir1])
    PressKey(dirs[dir2])
    time.sleep(random.randint(1, 5))
    ReleaseKey(dirs[dir1])
    ReleaseKey(dirs[dir2])
    
def TripleMove():
    dir1 = random.randint(0,(len(dirs) - 1))
    dir2 = random.randint(0,(len(dirs) - 1))
    dir3 = random.randint(0,(len(dirs) - 1))
    PressKey(dirs[dir1])
    PressKey(dirs[dir2])
    PressKey(dirs[dir3])
    time.sleep(random.randint(1, 5))
    ReleaseKey(dirs[dir1])
    ReleaseKey(dirs[dir2])
    ReleaseKey(dirs[dir3])

def main():
    print('Running rn, please tab into gta and un-pause, starting in:')
    for i in list(range(10))[::-1]:
            print(i + 1)
            time.sleep(1)
    while True:
        movecount = random.randint(1,3)
        if movecount == 1:
            SingleMove()
        elif movecount == 2:
            DoubleMove()
        else:
            TripleMove()
        
        print("Still running :)")


if __name__ == "__main__":
    main()