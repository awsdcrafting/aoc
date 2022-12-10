#!/usr/bin/env python

input=[]
with open("input") as f:
    input = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""
    input = f.read().splitlines() # lines without \n



def solve1():
    interesting_cycles = [20, 60, 100, 140, 180, 220]
    x = 1
    cycle = 0
    total = 0
    for line in input:
        line = line.strip()
        cycle += 1
        if cycle in interesting_cycles:
            total += cycle * x
        if line == "noop":
            continue
        else:
            _, i = line.split(" ")#
            i = int(i)
            cycle += 1
            if cycle in interesting_cycles:
                total += cycle * x
            x += i
    while cycle < interesting_cycles[-1]:
        cycle += 1
        if cycle in interesting_cycles:
            total += cycle * x
    print(f"{total=}")

def solve2():
    #lines = [["."] * 40] * 6 #references does not work
    lines = [["." for _ in range(40)] for _ in range(6)]
    x = 1
    cycle = 0
    for line in input:
        line = line.strip()
        y_pos = cycle // 40
        x_pos = cycle % 40
        if abs(x_pos - x) <= 1:
            lines[y_pos][x_pos] = "#"
        cycle += 1
        if line == "noop":
            continue
        else:
            y_pos = cycle // 40
            x_pos = cycle % 40
            if abs(x_pos - x) <= 1:
                lines[y_pos][x_pos] = "#"
            cycle += 1
            _, i = line.split(" ")#
            i = int(i)
            x += i
    
    print("\n".join(["".join(x) for x in lines]))
    #"EJCFPGLH"

if __name__=="__main__":
    solve1()
    solve2()


