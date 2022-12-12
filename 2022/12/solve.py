#!/usr/bin/env python
from queue import PriorityQueue
import math

input=[]
with open("input") as f:
    input="""Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""
    input = [[x for x in y] for y in f.read().splitlines()] # lines without \n
    print(input)
    start = None
    end = None
    starting_positions = []
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == "S":
                start = (x, y)
                starting_positions += [(x, y)]
            if input[y][x] == "E":
                end = (x, y)
            if input[y][x] == "a":
                starting_positions += [(x, y)]
    print(f"{start=} {end=}")

def height(x):
    if x == "S":
        return ord("a")
    if x == "E":
        return ord("z")
    return ord(x)

def dist(a, b):
    return abs(b[0] - a[0]) + abs(b[1]- a[1])

def get_path(path):
    ret = []
    current = end
    while current in path:
        ret += [current]
        current = path[current]
    ret += [current]
    ret.reverse()
    return ret

def neighbors(pos):
    ret = []
    if pos[0] > 0:
        ret += [(pos[0]-1, pos[1])]
    if pos[0] < len(input[1]) - 1:
        ret += [(pos[0] + 1, pos[1])]
    
    if pos[1] > 0:
        ret += [(pos[0], pos[1]-1)]
    if pos[1] < len(input) - 1:
        ret += [(pos[0], pos[1]+1)]

    return ret


def aStar(start, end, max_height_diff=1):
    open_nodes = []
    path = {}
    g_score = {}
    g_score[start] = 0
    f_score = {}
    f_score[start] = dist(start, end)
    
    open_nodes.append(start)
    while len(open_nodes) > 0:
        open_nodes.sort(key= lambda x: f_score[x] if x in f_score else math.inf)
        current = open_nodes.pop(0)
        if current == end:
            return get_path(path)

        for neighbor in neighbors(current):
            if height(input[neighbor[1]][neighbor[0]]) - height(input[current[1]][current[0]]) > max_height_diff:
                continue
            t_gscore = g_score[current] + 1
            if neighbor not in g_score or t_gscore < g_score[neighbor]:
                path[neighbor] = current
                g_score[neighbor] = t_gscore
                f_score[neighbor] = t_gscore + dist(neighbor, end)
                if neighbor not in open_nodes:
                    open_nodes.append(neighbor)
        
    return None

def solve1():
    path = aStar(start, end, 1)
    print(path)
    print(f"{(len(path)-1)=}")

def solve2():
    shortest_path = None
    for start in starting_positions:
        print(f"Checking: {start}")
        path = aStar(start, end)
        if path != None and (shortest_path == None or len(path) < len(shortest_path)):
            shortest_path = path
            
    print(f"{shortest_path}")
    print(f"{(len(shortest_path)-1)=}")
if __name__=="__main__":
    solve1()
    solve2()


