#!/usr/bin/env python

import math

input=[]
with open("input") as f:
    input = f.read().splitlines() # lines without \n

# input = """LLR

# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)""".splitlines()

# input = """LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)""".splitlines()

instructions = input[0]


def parse_node(line):
    current, next = line.split(" = ")
    left, right = next.replace("(", "").replace(")", "").split(", ")
    return (current, left, right)
nodes = {node[0]: (node[1], node[2])  for line in input[2:] if (node:=parse_node(line))}
print(nodes)

def solve1():
    print("-"*25)
    print(" "*9  + "Solve1")
    print("-"*25)
    start = "AAA"
    goal = "ZZZ"

    steps = 0
    current = start
    while current != goal:
        instruction = instructions[steps % len(instructions)]
        steps += 1
        if instruction == "L":
            current = nodes[current][0]
        else:
            current = nodes[current][1]
    print(steps)

def solve2():
    print("-"*25)
    print(" "*9  + "Solve2")
    print("-"*25)
    current_nodes = [node for node in nodes if node.endswith("A")]
    has_finished = False
    # steps = 0
    # while not has_finished:
    #     has_finished = True
    #     instruction = instructions[steps % len(instructions)]
    #     instruction = (0 if instruction == "L" else 1)
    #     steps += 1
    #     for idx, current in enumerate(current_nodes):
    #         current_nodes[idx] = nodes[current][instruction]
    #         if not current_nodes[idx].endswith("Z"):
    #             has_finished = False
    # print(steps)

    steps = []
    for idx, current in enumerate(current_nodes):
        current_steps = 0
        while not current.endswith("Z"):
            instruction = instructions[current_steps % len(instructions)]
            instruction = (0 if instruction == "L" else 1)
            current_steps += 1
            current = nodes[current][instruction]
        steps += [current_steps]
    print(steps)
    print(math.lcm(*steps))
    
if __name__=="__main__":
    solve1()
    solve2()


