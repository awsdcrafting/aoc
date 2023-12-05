#!/usr/bin/env python

import math

input=[]
with open("input") as f:
    input = f.read().splitlines() # lines without \n


def find_numbers(line: str, search):
    lowest = len(line)
    highest = -1
    lowest_best = ""
    highest_best = ""
    for i in range(len(search)):
        s = search[i]
        l_index = line.find(s)
        r_index = line.rfind(s)
        s_index = i
        if s_index < 9 and len(search) > 9:
            s_index += 9
        s_number = search[s_index]
            
        if l_index >= 0 and l_index < lowest:
            lowest = l_index
            lowest_best = s_number
        if r_index >= 0 and r_index > highest:
            highest = r_index
            highest_best = s_number
    number = lowest_best + highest_best
    return int(number)

def solve1():
    print("-"*25)
    print(" "*9  + "Solve1")
    print("-"*25)
    numbers = [[x for x in line if x.isdigit()] for line in input]
    number_sum = [int(number[0] + number[-1]) for number in numbers]
    #print(number_sum)
    print(sum(number_sum))
    search = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    test = [find_numbers(line, search) for line in input]
    #print(test)
    print(sum(test))
    pass



def solve2():
    print("-"*25)
    print(" "*9  + "Solve2")
    print("-"*25)
    search = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    numbers = [find_numbers(line, search) for line in input]
    print(sum(numbers))
    pass

if __name__=="__main__":
    solve1()
    solve2()


