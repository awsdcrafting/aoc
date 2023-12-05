#!/usr/bin/env python
import re

import time

start_time = time.perf_counter_ns()

input=[]
with open("input") as f:
    input = f.read().splitlines() # lines without \n

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

def find_number(line: str, start_pos):
    #print(f"pre {line=} {start_pos=}")
    start = start_pos
    end = start
    while line[start-1].isdigit() and start > 0:
        start -= 1
    while end < len(line) and line[end].isdigit():
        end += 1
    #print(f"post {line=} {start=} {end=} {line[start:end]=}")
    return (int(line[start:end]), start, end)

symbol = r"[^.\d]"

adjacent_numbers = {}
for idx, line in enumerate(input):
    for match in re.finditer(symbol, line):
        #print(match)
        start = match.start()
        numbers = {find_number(input[idx+j], start + i) for i in range(-1,2) for j in range(-1,2) if idx+j >= 0 and idx+j < len(input) and input[idx+j][start+i].isdigit()}
        numbers = [number[0] for number in numbers]
        key = (str(match.group()), idx, match.start(), match.end())
        symbol_str = str(match.group())
        if symbol_str not in adjacent_numbers:
            adjacent_numbers[symbol_str] = {}
        adjacent_numbers[symbol_str][key] = numbers
#print(adjacent_numbers)

def solve1():
    print("-"*25)
    print(" "*9  + "Solve1")
    print("-"*25)
    print(sum([sum(numbers) for dicts in adjacent_numbers.values() for numbers in dicts.values()]))
    pass

def solve2():
    print("-"*25)
    print(" "*9  + "Solve2")
    print("-"*25)
    print(sum([numbers[0] * numbers[1] for numbers in adjacent_numbers["*"].values() if len(numbers) == 2]))
    pass

if __name__=="__main__":
    solve1()
    solve2()
    
    end_time = time.perf_counter_ns()
    print(f"{end_time-start_time}ns {(end_time-start_time)/1000000}ms")
