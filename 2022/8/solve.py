#!/usr/bin/env python

input=[]
with open("input") as f:
    input = """30373
25512
65332
33549
35390"""
    input = [[int(y) for y in x.strip()] for x in f.read().splitlines()] # lines without \n f.read()
    print(input)



def solve1():
    total = 0
    total += len(input) * 2
    total += len(input[0]) * 2 - 4
    for y in range(1, len(input)-1):
        for x in range(1, len(input[y])-1):
            #todo: smarter algo
            current = input[y][x]
            yMod = y - 1
            visible = True
            while(yMod >= 0):
                if input[yMod][x] >= current:
                    visible = False
                    break
                yMod -= 1
            if visible:
                total += 1
                continue
            yMod = y + 1
            visible = True
            while(yMod < len(input)):
                if input[yMod][x] >= current:
                    visible = False
                    break
                yMod += 1
            if visible:
                total += 1
                continue
            xMod = x - 1
            visible = True
            while(xMod >= 0):
                if input[y][xMod] >= current:
                    visible = False
                    break
                xMod -= 1
            if visible:
                total += 1
                continue
            xMod = x + 1
            visible = True
            while(xMod < len(input[y])):
                if input[y][xMod] >= current:
                    visible = False
                    break
                xMod += 1
            if visible:
                total += 1
                continue

    print(f"{total=}")
            
    
    

def solve2():
    best_score = 0
    for y in range(1, len(input)-1):
        print(f"{y}/{len(input)}")
        for x in range(1, len(input[y])-1):
            #todo: smarter algo
            current = input[y][x]
            yMod = y - 1
            total_visible = 1
            visible = 0
            while(yMod >= 0):
                visible += 1
                if input[yMod][x] >= current:
                    break
                yMod -= 1
            total_visible *= visible
            visible = 0
            yMod = y + 1
            while(yMod < len(input)):
                visible += 1
                if input[yMod][x] >= current:
                    break
                yMod += 1
            xMod = x - 1
            total_visible *= visible
            visible = 0
            while(xMod >= 0):
                visible += 1
                if input[y][xMod] >= current:
                    break
                xMod -= 1
            xMod = x + 1
            total_visible *= visible
            visible = 0
            while(xMod < len(input[y])):
                visible += 1
                if input[y][xMod] >= current:
                    break
                xMod += 1
            total_visible *= visible
            visible = 0
            if total_visible > best_score:
                best_score = total_visible
                #print(f"{x=} {y=} {current}")
    print(f"{best_score=}")

if __name__=="__main__":
    solve1()
    solve2()


