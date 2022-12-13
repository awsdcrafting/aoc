#!/usr/bin/env python
import json
import functools

input=[]
with open("input") as f:
    input="""[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""
    input = [[json.loads(y) for y in x.splitlines()] for x in f.read().split("\n\n")] # lines without \n
    print(input)

def compare_list(left, right, debug=False, depth=0):
    prefix = ' '*(4*depth)
    if debug:
        print(f"{prefix}{left=} {right=}")
    for i in range(max(len(left), len(right))):
        if i >= len(left):
            if debug:
                print(f"{prefix}left is shorter => True")
            return True
        if i >= len(right):
            if debug:
                print(f"{prefix}right is shorter => False")
            return False
        lefti = left[i]
        righti = right[i]
        if debug:
            print(f"{prefix}{lefti=} {righti=}")
        if isinstance(lefti, int) and isinstance(righti, int):
            if debug:
                print(f"{prefix}both are ints")
            if lefti < righti:
                if debug:
                    print(f"{prefix}left is smaller => True")
                return True
            elif lefti > righti:
                if debug:
                    print(f"{prefix}right is smaller => False")
                return False
            continue
        if isinstance(lefti, int) and not isinstance(righti, int):
            if debug:
                print(f"{prefix}left is int right is not")
            lefti = [lefti]
            cmp = compare_list(lefti, righti, debug=debug, depth=depth+1)
            if cmp != None:
                return cmp
            continue
        if not isinstance(lefti, int) and isinstance(righti, int):
            if debug:
                print(f"{prefix}left is not int right is")
            righti = [righti]
            cmp = compare_list(lefti, righti, debug=debug, depth=depth+1)
            if cmp != None:
                return cmp
            continue
        #both are lists
        if debug:
            print(f"{prefix}both are not ints")
        cmp = compare_list(lefti, righti, debug=debug, depth=depth+1)
        if cmp != None:
            return cmp
    return None
            
def cmp_lists(left, right):
    cmp = compare_list(left, right)
    if cmp:
        return -1
    elif cmp == None:
        return 0
    else:
        return 1

def test():
    left=[9]
    right = [[8, 7, 6]]
    compare_list(left, right, True)
    

def solve1():
    total = 0
    index = 1
    for packets in input:
        left, right = packets
        if compare_list(left, right):
            #print(f"correct: {left=} {right=}")
            total += index
        index+=1
            
    print(f"{total=}")
def solve2():
    new_input = [item for sublist in input for item in sublist] #flatten by one
    #print(new_input)
    new_input += [[[2]], [[6]]]
    new_input.sort(key=functools.cmp_to_key(cmp_lists))
    #print(new_input)
    total = 1
    for i in range(len(new_input)):
        if new_input[i] == [[2]]:
            total *= (i+1)
        if new_input[i] == [[6]]:
            total *= (i+1)
            
    print(f"{total=}")
if __name__=="__main__":
    solve1()
    solve2()
    
    #test()


