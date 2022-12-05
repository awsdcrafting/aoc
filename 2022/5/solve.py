#!/usr/bin/env python
import re


input=[]
with open("input") as f:
    input = f.read()
    input1, input2 = input.split("\n\n")
    input1 = input1.split("\n")
    input1 = list(map(lambda str: [str[x] for x in range(len(str)) if x % 4 == 1], input1)) # only the container char
    #print(input1)
    input1 = ["".join([row[i] for row in input1]).strip() for i in range(len(input1[0]))] # convert to columns in str form
    #print(input1)
    input1 = dict(map(lambda i: (int(input1[i][-1]), input1[i][:len(input1[i])-1]), range(len(input1))))  # convert to dict with column number as key
    #print(input1)
    #print(input2)
    input2 = input2.strip().replace("move", "").replace("from", "").replace("to", "")
    input2 = input2.split("\n")
    input2 = list(map(lambda str: [int(x) for x in re.split("\s+", str.strip())], input2))# array of 'count from to'


def single_move(move, dict):
    count, fr, to = move
    fr_str = dict[fr]
    to_str = dict[to]
    while count > 0:
        count-=1
        to_str = fr_str[0] + to_str
        fr_str = fr_str[1:]
    dict[to] = to_str
    dict[fr] = fr_str

def solve1():
    input_dict = input1.copy()
    for moves in input2:
        single_move(moves, input_dict)
    out = "".join([x[0] for x in input_dict.values()])
    print(out)

def multi_move(move, dict):
    count, fr, to = move
    fr_str = dict[fr]
    to_str = dict[to]
    
    to_str = fr_str[:count] + to_str
    fr_str = fr_str[count:]
    
    dict[to] = to_str
    dict[fr] = fr_str
    

def solve2():
    input_dict = input1.copy()
    for moves in input2:
        multi_move(moves, input_dict)
    out = "".join([x[0] for x in input_dict.values()])
    print(out)

if __name__=="__main__":
    solve1()
    solve2()


