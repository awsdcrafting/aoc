#!/usr/bin/env python

input=[]
with open("input") as f:
    input = f.read().splitlines() # lines without \n

#A = ROCK = X 0
#B = PAPER = Y 1
#C = SCISSORS = Z 2


def points(a, b):
    if a == b:
        return 3 + (b+1)
    elif (a+1)%3 == b:
        return 6 + (b+1)
    else:
        return 0 + (b+1)
            
def encode(str):
    if str == "A" or str == "X":
        return 0
    elif str == "B" or str == "Y":
        return 1
    elif str == "C" or str == "Z":
        return 2
    else:
        print(f"ERROR {str}")
        return -1
    
    
def solve1():
    total = 0
    for line in input:
        a, b = line.split(" ", 1)
        av = encode(a)
        bv = encode(b)
        total += points(av, bv)
        
    print(f"{total=}")
        

#X = LOOSE
#Y = DRAW
#Z = WIN

def solve2():
    total = 0
    for line in input:
        a, b = line.split(" ", 1)
        av = encode(a)
        if b == "X":
            bv = (av - 1) % 3
        elif b == "Y":
            bv = av
        elif b == "Z":
            bv = (av + 1) % 3
        else:
            print(f"ERROR {str}")
        total += points(av, bv)
    
    print(f"{total=}")

if __name__=="__main__":
    solve1()
    solve2()


