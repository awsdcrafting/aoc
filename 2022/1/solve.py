#!/usr/bin/env python

input=[]
with open("input") as f:
    input = f.read().splitlines() # lines without \n


def solve1():
    current_cal = 0
    most_cal = 0
    total_cal = 0
    index = 0
    most_index = 0
    for line in input:
        if not line.strip():
            index += 1
            if current_cal > most_cal:
                most_cal = current_cal
                most_index = index
            current_cal = 0
            continue
        current_cal += int(line.strip())

    print(f"{most_cal=} {total_cal=} {most_index=}")

def solve2():
    most_amount =  3
    most_cals = []
    current_cal = 0
    
    for line in input:
        if not line.strip():
            if len(most_cals) < most_amount:
                most_cals += [current_cal]
            else:
                m = min(most_cals)
                type(m)
                if m >= current_cal:
                    current_cal = 0
                    continue
                for i in range(most_amount):
                    if most_cals[i] == m:
                        most_cals[i] = current_cal
                        break
            current_cal = 0
            continue
        current_cal += int(line.strip())
    
    print(len(most_cals))
    print(sum(most_cals))
            

if __name__=="__main__":
    solve1()
    solve2()


