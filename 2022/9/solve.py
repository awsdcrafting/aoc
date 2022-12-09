#!/usr/bin/env python


input=[]
with open("input") as f:
    input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
    input = f.read().strip().splitlines() # lines without \n
    

def tail_pos(h_pos, old_pos):
    x_dist = h_pos[0] - old_pos[0]
    abs_x_dist = abs(x_dist)
    y_dist = h_pos[1] - old_pos[1]
    abs_y_dist = abs(y_dist)
    if abs_x_dist > 1 or abs_y_dist > 1:
        if abs_x_dist == 0:
            abs_x_dist = 1
        if abs_y_dist == 0:
            abs_y_dist = 1
        return (int(old_pos[0] + (x_dist/abs_x_dist)), int(old_pos[1] + (y_dist / abs_y_dist)))
    return old_pos
            
def simulate_rope(length):
    positions = set()
    knots = []
    for _ in range(length):
        knots += [(0,0)]
    positions.add(knots[len(knots)-1])
    for line in input:
        direction, step = line.split(" ")
        step = int(step)
        while (step > 0):
            if direction == "R":
                knots[0] = (knots[0][0] + 1, knots[0][1])
            elif direction == "L":
                knots[0] = (knots[0][0] - 1, knots[0][1])
            elif direction == "U":
                knots[0] = (knots[0][0], knots[0][1] + 1)
            elif direction == "D":
                knots[0] = (knots[0][0], knots[0][1] - 1)
            for i in range(len(knots)-1):
                knots[i+1] = tail_pos(knots[i], knots[i+1])
                if i == len(knots)-2:
                    positions.add(knots[len(knots)-1])
            #print(knots)
            step -= 1
    return positions


def solve1():
    print(len(simulate_rope(2)))
                
def solve2():
    print(len(simulate_rope(10)))

if __name__=="__main__":
    solve1()
    solve2()


