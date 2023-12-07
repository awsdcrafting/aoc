#!/usr/bin/env python
from dataclasses import dataclass
import functools

input=[]
with open("input") as f:
    input = f.read().splitlines() # lines without \n

# input = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483""".splitlines()

strength = {"2":1, "3":2, "4":3, "5":4, "6":5, "7":6, "8":7, "9":8, "T":9, "J":10, "Q":11, "K":12, "A":13}

hand_type = {"HIGH":1, "ONE":2, "TWO":3, "THREE":4, "FULL_HOUSE":5, "FOUR":6, "FIVE":7}

@dataclass
@functools.total_ordering
class Hand:
    hand: str
    hand_type: str
    bet: int

    def __eq__(self, other):
        diff = hand_type[self.hand_type] - hand_type[other.hand_type] 
        if diff:
            return False
        for idx in range(len(self.hand)):
            if self.hand[idx] != other.hand[idx]:
                return False
        return True

    def __gt__(self, other):
        diff = hand_type[self.hand_type] - hand_type[other.hand_type]
        if diff > 0:
            return True
        if diff < 0:
            return False
        for idx in range(len(self.hand)):
            diff = strength[self.hand[idx]] - strength[other.hand[idx]]
            if diff > 0:
                return True
            if diff < 0:
                return False
        return False

def find_type(hand: str, joker):
    symbols = {}
    for symbol in hand:
        current = symbols.setdefault(symbol, 0)
        current += 1
        symbols[symbol] = current
    joker_count = 0
    if joker:
        joker_count = symbols.setdefault("J", 0)
        del symbols["J"]
    
    values = [x for x in symbols.values()]
    values.sort()
    values.reverse()
    for idx, value in enumerate(values):
        joker_value = (joker * joker_count) + value
        if value == 5 or joker_value == 5:
            return "FIVE"
        if value == 4 or joker_value == 4:
            return "FOUR"
        if value == 3 and 2 in values:
            return "FULL_HOUSE"
        joker_needed = 3 - value
        remaining_jokers = joker_count - joker_needed
        if remaining_jokers >= 0 and values[idx+1] + remaining_jokers == 2:
            return "FULL_HOUSE"
        if value == 3 or joker_value == 3:
            return "THREE"
        if value == 2 and len(symbols) == 3:
            return "TWO"
        joker_needed = 2-value
        remaining_jokers = joker_count - joker_needed
        if remaining_jokers >= 0 and values[idx+1] + remaining_jokers == 2:
            return "TWO"
        if value == 2 or joker_value == 2:
            return "ONE"
    if joker_count == 5:
        return "FIVE"
    return "HIGH"
    

def parse_hand(line: str, joker=False):
    hand, bet = line.split()
    bet = int(bet)
    return Hand(hand, find_type(hand, joker), bet)


def solve1():
    print("-"*25)
    print(" "*9  + "Solve1")
    print("-"*25)
    hands = [parse_hand(line) for line in input]
    hands.sort()
    worths = [(idx+1) * hand.bet for idx, hand in enumerate(hands)]
    print(sum(worths))
    pass

def solve2():
    print("-"*25)
    print(" "*9  + "Solve2")
    print("-"*25)
    strength["J"] = 0
    hands = [parse_hand(line, True) for line in input]
    hands.sort()
    #print(hands)
    worths = [(idx+1) * hand.bet for idx, hand in enumerate(hands)]
    print(sum(worths))
    pass

if __name__=="__main__":
    solve1()
    solve2()


