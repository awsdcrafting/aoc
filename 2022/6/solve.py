#!/usr/bin/env python

input=[]
with open("input") as f:
    input = f.read().strip() # lines without \n

def detect(length):
    for i in range(length, len(input)+1):
        if len(set(input[i-length:i])) == length:
            return i

def solve1():
    print(detect(4))

def solve2():
    print(detect(14))

if __name__=="__main__":
    solve1()
    solve2()


