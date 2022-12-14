#!/usr/bin/env python
import math

input=[]
with open("input") as f:
    input = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""
    input = [[[int(z) for z in y.strip().split(",") ] for y in x.split("->") ] for x in f.read().splitlines()] # lines without \n
    sand = (500,0)
    min_x = min([item[0] for sublist in input for item in sublist])
    min_x = min(sand[0], min_x)
    max_x = max([item[0] for sublist in input for item in sublist])
    max_x = max(sand[0], max_x)
    min_y = min([item[1] for sublist in input for item in sublist])
    min_y = min(sand[1], min_y)
    max_y = max([item[1] for sublist in input for item in sublist])
    max_y = max(sand[1], max_y)
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    sand = (sand[0] - min_x, sand[1] - min_y)
    print(input)
    input = [[(coord[0] - min_x, coord[1] - min_y) for coord in line] for line in input]
    print(input)


def add_sand(grid, pos=sand):
    moved = True
    start_pos = pos
    while moved:
        if pos[1] + 1 >= len(grid):
            moved = False
            return False # infinity
        if grid[pos[1]+1][pos[0]] == ".":
            pos = (pos[0], pos[1] + 1)
            continue
        if pos[0] - 1 < 0:
            moved = False
            return False # infinity
        if grid[pos[1]+1][pos[0]-1] == ".":
            pos = (pos[0]-1, pos[1] + 1)
            continue
        if pos[0] + 1 >= len(grid[0]):
            moved = False
            return False # infinity
        if grid[pos[1]+1][pos[0]+1] == ".":
            pos = (pos[0]+1, pos[1] + 1)
            continue
        moved = False
    grid[pos[1]][pos[0]] = "o"
    if pos == start_pos:
        return False
    return True #settled
        

def solve1():
    
    grid = [["." for x in range(width)] for y in range(height)]
    grid[sand[1]][sand[0]] = "+"
    print("\n".join(["".join(line) for line in grid]))
    
    print(f"{min_x=} {max_x=} {min_y=} {max_y=} {width=} {height=}")
    for line in input:
        for i in range(len(line)-1):
            start = line[i]
            stop = line[i+1]
            for x in range(abs(stop[0] - start[0]) + 1):
                x_pos = start[0] + int(math.copysign(x, stop[0] - start[0]))
                for y in range(abs(stop[1] - start[1]) + 1):
                    y_pos = start[1] + int(math.copysign(y, stop[1] - start[1]))
                    grid[y_pos][x_pos] = "#"
                    
    print("\n".join(["".join(line) for line in grid]))
    moved = 0
    while add_sand(grid):
        moved += 1
        
    print("\n".join(["".join(line) for line in grid]))
    print(f"{moved=}")
    
def solve2():
    global height
    global sand
    global width
    height += 2
    extra = height * 2 - width + 1
    sand = (sand[0] + extra // 2, sand[1])
    print(f"{width=} {sand[0]=}")
    center = ((width + extra) // 2) - sand[0]
    print(center)
    grid = [["." for x in range(width + extra)] for y in range(height)]
    
    sand = (sand[0] + center, sand[1])
    grid[sand[1]][sand[0]] = "+"
    
    for line in input:
        for i in range(len(line)-1):
            start = line[i]
            stop = line[i+1]
            for x in range(abs(stop[0] - start[0]) + 1):
                x_pos = start[0] + int(math.copysign(x, stop[0] - start[0]))
                x_pos += int(math.copysign(extra, x) // 2)
                x_pos += center
                for y in range(abs(stop[1] - start[1]) + 1):
                    y_pos = start[1] + int(math.copysign(y, stop[1] - start[1]))
                    grid[y_pos][x_pos] = "#"
        
    for x in range(len(grid[-1])):
        grid[-1][x] = "#"
    
    print("\n".join(["".join(line) for line in grid]))
    moved = 1
    while add_sand(grid, (sand[0], sand[1])):
        moved += 1

    print("\n".join(["".join(line) for line in grid]))
    print(f"{moved=}")

if __name__=="__main__":
    solve1()
    solve2()


