#!/usr/bin/env python

input=[]
with open("input") as f:
    input = f.read().splitlines() # lines without \n


def parseRange(r):
    a1, a2 = r.split("-")
    return (int(a1), int(a2))

def solve1():
    total = 0
    for line in input:
        r1, r2 = line.split(",", 2)
        r1 = parseRange(r1)
        r2 = parseRange(r2)
        if r1[0] <= r2[0] and r1[1] >= r2[1]:
            total += 1
        elif r2[0] <= r1[0] and r2[1] >= r1[1]:
            total += 1
    print(f"{total=}")
        

def solve2():
    total = 0
    for line in input:
        r1, r2 = line.split(",", 2)
        r1 = parseRange(r1)
        r2 = parseRange(r2)
        if r1[0] >= r2[0] and r1[0] <= r2[1]:
            total += 1
        elif r1[1] >= r2[0] and r1[1] <= r2[1]:
            total += 1
        elif r2[0] >= r1[0] and r2[0] <= r1[1]:
            total += 1
        elif r2[1] >= r1[0] and r2[1] <= r1[1]:
            total += 1
    print(f"{total=}")

if __name__=="__main__":
    solve1()
    solve2()


