#!/usr/bin/env python

input=[]
with open("input") as f:
    input = f.read().splitlines() # lines without \n

# input = """Time:      7  15   30
# Distance:  9  40  200""".splitlines()



def solve1():
    print("-"*25)
    print(" "*9  + "Solve1")
    print("-"*25)
    times = [int(x) for x in input[0].split(":")[1].split()]
    distance = [int(x) for x in input[1].split(":")[1].split()]

    games = [x for x in zip(times, distance)]
    prod = 1
    for game in games:
        print(game)
        wins = 0
        for i in range(game[0]):
            if i * (game[0] - i) > game[1]:
                wins += 1
        prod *= wins
    print(prod)
    pass

def solve2():
    print("-"*25)
    print(" "*9  + "Solve2")
    print("-"*25)
    time = int(input[0].replace(" ", "").split(":")[1])
    distance = int(input[1].replace(" ", "").split(":")[1])
    wins = 0
    for i in range(time):
        if i * (time - i) > distance:
                wins += 1
    print(wins)
if __name__=="__main__":
    solve1()
    solve2()


