#!/usr/bin/env python
import re
import pprint

input=[]
with open("input") as f:
    input = f.read().splitlines() # lines without \n
    
#test_input
# input = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..""".splitlines()

part_positions = {}
number_positions = []
adjacent_numbers = {}


number = r"\d+"
symbol = r"[^.\d]"

positions = []
for idx, line in enumerate(input):
    number_positions += [(int(m.group()), idx, m.start(), m.end()) for m in re.finditer(number, line)]
    #print(idx+1)
    symbol_positions = [(str(m.group()), idx, m.start(), m.end()) for m in re.finditer(symbol, line)]
    for part_symbol, line_number, start, end in symbol_positions:
        if part_symbol not in part_positions:
            part_positions[part_symbol] = []
        positions = part_positions[part_symbol]
        positions += [(part_symbol, line_number, start, end)]
        part_positions[part_symbol] = positions

def is_adjacent(pos1, pos2):
    if pos1[1] == pos2[1]:
        return pos1[2] == pos2[3] or pos1[3] == pos2[2]
    elif pos1[1] == pos2[1] - 1 or pos1[1] == pos2[1] + 1:
        return (pos1[2] >= pos2[2] and pos1[2] <= pos2[3]) or (pos1[3] >= pos2[2] and pos1[3] <= pos2[3]) or (pos2[2] >= pos1[2] and pos2[2] <= pos1[3]) or (pos2[3] >= pos1[2] and pos2[3] <= pos1[3]) 
    return False

for part_symbol, positions in part_positions.items():
    adjacents = []
    for position in positions:
        adjacents += [(position, [number for number in number_positions if is_adjacent(number, position)])]
    adjacent_numbers[part_symbol] = adjacents

pprint.pprint(adjacent_numbers)

def solve1():
    print("-"*25)
    print(" "*9  + "Solve1")
    print("-"*25)
    print(sum([o[0] for m in adjacent_numbers.values() for n in m for o in n[1]]))
    pass

def solve2():
    print("-"*25)
    print(" "*9  + "Solve2")
    print("-"*25)
    values = adjacent_numbers["*"]
    print(sum([x[1][0][0]*x[1][1][0] for x in values if len(x[1]) == 2]))
    
    pass

if __name__=="__main__":
    solve1()
    solve2()


