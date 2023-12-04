#!/usr/bin/env python
from dataclasses import dataclass
import math


input=[]
with open("input") as f:
    input = f.read().splitlines() # lines without \n

# input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".splitlines()

@dataclass
class Card:
    id: int
    winning_numbers: list
    numbers: list
    count: int

def parse_card(str: str):
    card, numbers = str.split(":", 2)
    card_id = int(card.split()[1])
    winning_numbers, numbers = numbers.split("|")
    winning_numbers =  [int(n) for n in winning_numbers.strip().split()]
    numbers =  [int(n) for n in numbers.strip().split()]
    return Card(card_id, winning_numbers, numbers, 1)

cards = [parse_card(line) for line in input]
#print(cards)

def solve1():
    print("-"*25)
    print(" "*9  + "Solve1")
    print("-"*25)
    print(sum([math.floor(math.pow(2,len(set(card.numbers).intersection(set(card.winning_numbers)))-1)) for card in cards]))
    
    pass

def solve2():
    print("-"*25)
    print(" "*9  + "Solve2")
    print("-"*25)
    for idx, card in enumerate(cards):
        winning_count = len(set(card.numbers).intersection(set(card.winning_numbers)))
        for i in range(winning_count):
            if i > len(cards):
                break
            cards[idx+i+1].count += card.count
    print(sum([card.count for card in cards]))

if __name__=="__main__":
    solve1()
    solve2()


