#!/usr/bin/env python
from dataclasses import dataclass

import math

input=[]
with open("input") as f:
    input = f.read().splitlines() # lines without \n

@dataclass
class Record:
    cube_amount: dict

@dataclass
class GameInformation:
    id: int
    records: list[Record]

def parse_record(str: str):
    information = [s.strip().split(" ") for s in str.split(",")]
    information = {info[1]:int(info[0]) for info in information}
    record = Record(information)
    return record
    
def parse_game(str):
    if not str:
        return None
    game, records = str.split(":", 2)
    records = records.split(";")
    game_id = int(game.split(" ")[1])
    records = [parse_record(record) for record in records]
    game_information = GameInformation(game_id, records)
    return game_information
    

games = [parse_game(line) for line in input]

def solve1():
    print("-"*25)
    print(" "*9  + "Solve1")
    print("-"*25)
    def filter_game(game):
        max_contains = {"red": 12, "green": 13, "blue": 14}
        for record in game.records:
            for cube, amount in max_contains.items():
                if cube in record.cube_amount and record.cube_amount[cube] > amount:
                    return False
        return True
    filtered = [game for game in games if filter_game(game)]
    print(sum([game.id for game in filtered if game]))
    pass

def solve2():
    print("-"*25)
    print(" "*9  + "Solve2")
    print("-"*25)

    def calculate_power(game):
        min_amount = {}
        for record in game.records:
            for cube, amount in record.cube_amount.items():
                if cube not in min_amount or amount > min_amount[cube]:
                    min_amount[cube] = amount
        return math.prod(min_amount.values())
    print(sum([calculate_power(game) for game in games]))
    pass

if __name__=="__main__":
    solve1()
    solve2()


