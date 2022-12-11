#!/usr/bin/env python
import dataclasses
from dataclasses import dataclass
import copy
import math
import functools

@dataclass
class Monkey():
    item_list: list = dataclasses.field(default_factory=list)
    operation:str = ""
    test: int = 1
    true:int = 0
    false:int = 0
    throw_counter:int = 0
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def throw_items(self, monkeys, divisor = 3, mod=0):
        while len(self.item_list) > 0:
            item = self.item_list.pop(0)
            op, arg = self.operation.split()
            if op == "*":
                if arg == "x":
                    item *= item
                else:
                    item *= int(arg)
            elif op == "+":
                if arg == "x":
                    item += item
                else:
                    item += int(arg)
            item //= divisor
            if mod != 0:
                item %= mod
            if item % self.test == 0:
                monkeys[self.true].item_list += [item]
            else:
                monkeys[self.false].item_list += [item]
            self.throw_counter += 1
input=[]
with open("input") as f:
    input = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""
    input = [x.splitlines() for x in f.read().split("\n\n")] # lines without \n
    #print(input)
    monkeys = []
    for info in input:
        monkey = Monkey()
        for line in info:
            line = line.strip()
            if line.startswith("Monkey"):
                continue
            if line.startswith("Starting items:"):
                _, items = line.split(":")
                items = [int(x.strip()) for x in items.strip().split(",")]
                monkey.item_list = items
                continue
            if line.startswith("Operation:"):
                line = line[line.index("new = old")+len("new = old"):].replace("old", "x")
                #print(line)
                #print(f"{op=} {arg=}")
                monkey.operation = line
            if line.startswith("Test"):
                line = line[len("Test: divisible by "):]
                monkey.test = int(line)
            if line.startswith("If true:"):
                line = line[len("If true: throw to monkey "):]
                b = int(line)
                monkey.true = b
            if line.startswith("If false:"):
                line = line[len("If false: throw to monkey "):]
                c = int(line)
                monkey.false = c
        monkeys += [monkey]
    
                


def solve1():
    monkey_list = []
    divisor = 1
    for monkey in monkeys:
        monkey_list += [copy.deepcopy(monkey)]
        divisor *= monkey.test
        
    #print(monkey_list)
    for _ in range(20):
        for monkey in monkey_list:
            monkey.throw_items(monkey_list,3, divisor)
    monkey_list.sort(key= lambda x: x.throw_counter, reverse=True)
    #print(monkey_list)
    print(f"{(monkey_list[0].throw_counter * monkey_list[1].throw_counter)=}")
    

def solve2():
    monkey_list = []
    divisor = 1
    for monkey in monkeys:
        monkey_list += [copy.deepcopy(monkey)]
        divisor *= monkey.test
    #print(divisor)
    #print(monkey_list)
    for i in range(10_000):
        for monkey in monkey_list:
            monkey.throw_items(monkey_list,1, divisor)
            
    #print(monkey_list)
    monkey_list.sort(key= lambda x: x.throw_counter, reverse=True)
    print(f"{(monkey_list[0].throw_counter * monkey_list[1].throw_counter)=}")

if __name__=="__main__":
    solve1()
    solve2()


