#!/usr/bin/env python

from os import walk
import pprint

input=[]
with open("input") as f:
    input = f.read().splitlines() # lines without \n

# input = """-L|F7
# 7S-7|
# L|7||
# -L-J|
# L|-JF""".splitlines()

# input ="""7-F7-
# .FJ|7
# SJLL7
# |F--J
# LJ.LJ
# """.splitlines()

# input ="""..........
# .S------7.
# .|F----7|.
# .||....||.
# .||....||.
# .|L-7F-J|.
# .|..||..|.
# .L--JL--J.
# ..........""".splitlines()

connections = {
    "|": "NS",
    "-": "EW",
    "L": "NE",
    "J": "NW",
    "7": "SW",
    "F": "SE",
    "S": "NSEW",
    ".": "",
}

def get_opposite_dir(direction):
    if direction == "N":
        return "S"
    if direction == "S":
        return "N"
    if direction == "E":
        return "W"
    if direction == "W":
        return "E"
    return ""

def direction_to_matrix_change(direction):
    #format x y
    if direction == "N":
        return (0, -1)
    if direction == "S":
        return (0, 1)
    if direction == "E":
        return (1, 0)
    if direction == "W":
        return (-1, 0)
    return (0, 0)

def matrix_change_to_direction(change):
    if change == (0, -1):
        return "N"
    if change == (0, 1):
        return "S"
    if change == (1, 0):
        return "E"
    if change ==(-1, 0):
        return  "W"
    return ""

connection_matrix = {}

for connection in connections:
    connection_matrix[connection] = {}
    for direction in connections[connection]:
        direction_connections = []
        for other_connection in connections:
            if other_connection == "S":
                continue
            if get_opposite_dir(direction) in connections[other_connection]:
                direction_connections.append(other_connection)
        connection_matrix[connection][direction] = direction_connections

pprint.pprint(connection_matrix)

starting_pos = (-1, -1)
for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char == "S":
            starting_pos = (x, y)
            break
    if starting_pos != (-1, -1):
        break



def get_char(point):
    x, y = point
    if y < 0 or y >= len(input):
        return ""
    if x < 0 or x >= len(input[y]):
        return ""
    return input[y][x]

def get_connected(point):
    char = get_char(point)
    if not char:
        return []
    x, y  = point
    connected = []
    char = input[y][x]
    for direction in connection_matrix[char]:
        dx, dy = direction_to_matrix_change(direction)
        new_pos = (x + dx, y+dy)
        new_char = get_char(new_pos)
        if new_char and new_char in connection_matrix[char][direction]:
            connected.append(new_pos)
    return connected

print(starting_pos)

def bfs():
    nodes = {} #format point: dist
    stack = [(starting_pos, 0)]
    while len(stack) > 0:
        current, dist = stack.pop(0)
        nodes[current] = dist
        for connected in get_connected(current):
            if connected in nodes:
                continue
            stack.append((connected, dist+1))
    return nodes

nodes = bfs()

def is_enclosed(point):
    pass

enclosed = {}


#pprint.pprint(nodes)


mappings = {
    "|": "│",
    "-": "─",
    "L": "└",
    "J": "┘",
    "7": "┐",
    "F": "┌",
    ".": ".",
    "S": "S"
}
print()
#print("\n".join(["".join([str(nodes[(x, y)]) if (x, y) in nodes else "." for x in range(len(input[y]))]) for y in range(len(input))]))
print()
loop = "\n".join(["".join([mappings[input[y][x]] if (x, y) in nodes else "." for x in range(len(input[y]))]) for y in range(len(input))])

loop_start_connections = [matrix_change_to_direction((new_pos[0] - starting_pos[0], new_pos[1] - starting_pos[1])) for new_pos in get_connected(starting_pos)]

new_value = "S"
if "N" in loop_start_connections:
    if "E" in loop_start_connections:
        new_value = "└"
    elif "W" in loop_start_connections:
        new_value = "┘"
    elif "S" in loop_start_connections:
        new_value = "│"
elif "S" in loop_start_connections:
    if "E" in loop_start_connections:
        new_value = "┌"
    elif "W" in loop_start_connections:
        new_value = "┐"
else:
    new_value = "─"

loop = loop.replace("S", new_value)
print(loop)

loop_lines = loop.splitlines()

expanded = ""
for y in range(len(input) * 2):
    line = ""
    for x in range(len(input[y//2]) * 2):
        if y // 2 == y/2 and x//2 == x/2:
            line += loop_lines[y//2][x//2]
        elif y // 2 == y/2:
            if loop_lines[y//2][x//2] in ["─", "└", "┌"] and loop_lines[y//2][(x+1)//2] in ["─", "┘", "┐"]:
                line += "─"
            else:
                line += "□"
        elif x // 2 == x/2:
            if loop_lines[y//2][x//2] in ["│", "┐", "┌"] and loop_lines[(y+1)//2][x//2] in ["│", "┘", "└"]:
                line += "│"
            else:
                line += "■"
        else:
            line += "+"
    expanded += line + "\n"

print(expanded)

expanded_lines = expanded.splitlines()

def solve1():
    print("-"*25)
    print(" "*9  + "Solve1")
    print("-"*25)
    print(max(nodes.values()))
    pass

def solve2():
    print("-"*25)
    print(" "*9  + "Solve2")
    print("-"*25)
    def walkable(char):
        return char in ".+□■"

    enclosed = {}

    def enclosed_bfs(point):
        visited = []
        queue = [point]
        breakout = False
        dots = []
        while len(queue) > 0:
            #print(len(queue), len(visited))
            current = queue.pop()
            x, y = current
            visited.append(current)
            if expanded_lines[y][x] == ".":
                dots.append(current)
            for dy in range(-1, 2):
                newy = y + dy
                if newy < 0 or newy >= len(expanded_lines):
                    breakout = True
                    continue
                for dx in range(-1, 2):
                    newx = x + dx
                    if newx < 0 or newx >= len(expanded_lines[newy]):
                        breakout = True
                        continue
                    new = (newx, newy)
                    if new not in visited and new not in queue and walkable(expanded_lines[newy][newx]):
                        queue.append(new)
        for dot in dots:
            enclosed[dot] = not breakout
    print(f"{len(expanded_lines), len(expanded_lines[0])}")
    for y, line in enumerate(expanded_lines):
        for x, char in enumerate(line):
            if char == "." and (x, y) not in enclosed:
                print(f"bfs: {y=} {x=}")
                enclosed_bfs((x, y))
            elif char == ".":
                pass
                #print(f"rejected found: {y=} {x=}")
            else:
                pass
                #print(f"rejected char: {y=} {x=}")
    print(sum(enclosed.values()))

if __name__=="__main__":
    solve1()
    solve2()


