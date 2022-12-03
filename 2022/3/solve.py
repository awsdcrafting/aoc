#!/usr/bin/env python

input=[]
with open("input") as f:
    input = f.read().splitlines() # lines without \n


def prio(x):
    o = ord(x)
    if o >= 97:
        o -= 96
    else:
        o -= 38
    return o

def solve1():
    total = 0
    for line in input:
        #line = line.swapcase()
        half = len(line)//2
        left = line[:half]
        right = line[half:]
        for x in left:
            if x in right:
                o = prio(x)
                total += o
                #print(f"{x=} {total=}")
                break
        #break
    print(f"{total=}")

def solve2():
    total = 0
    idx = 0
    while idx < len(input):
        line1 = input[idx]
        line2 = input[idx+1]
        line3 = input[idx+2]
        idx += 3
        for x in line1:
            if x in line2 and x in line3:
                total += prio(x)
                break
    print(f"{total=}")

if __name__=="__main__":
    solve1()
    solve2()


