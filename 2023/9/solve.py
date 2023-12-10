#!/usr/bin/env python

input=[]
with open("input") as f:
    input = f.read().splitlines() # lines without \n

# input = """0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45""".splitlines()


sequences = [[int(x) for x in line.split()] for line in input]




def solve1():
    print("-"*25)
    print(" "*9  + "Solve1")
    print("-"*25)
    sum = 0

    def next_sequence(sequence: list):
        next_sequence = []
        for idx in range(len(sequence) - 1):
            next_sequence += [sequence[idx+1] - sequence[idx]]
        return next_sequence
    for sequence in sequences:
        next_sequences = [sequence]
        current_sequence = sequence
        new_sequence = next_sequence(current_sequence)
        while any(new_sequence):
            next_sequences.append(new_sequence)
            current_sequence = new_sequence
            new_sequence = next_sequence(current_sequence)
        #print(next_sequences)
        for idx in range(len(next_sequences)-2, -1, -1):
            next_sequences[idx].append(next_sequences[idx][-1] + next_sequences[idx+1][-1])
        #print(next_sequences)
        sum += next_sequences[0][-1]
    print(sum)

def solve2():
    print("-"*25)
    print(" "*9  + "Solve2")
    print("-"*25)
    sum = 0

    def next_sequence(sequence: list):
        next_sequence = []
        for idx in range(len(sequence) - 1):
            next_sequence += [sequence[idx+1] - sequence[idx]]
        return next_sequence
    for sequence in sequences:
        sequence.reverse()
        next_sequences = [sequence]
        current_sequence = sequence
        new_sequence = next_sequence(current_sequence)
        while any(new_sequence):
            next_sequences.append(new_sequence)
            current_sequence = new_sequence
            new_sequence = next_sequence(current_sequence)
        #print(next_sequences)
        for idx in range(len(next_sequences)-2, -1, -1):
            next_sequences[idx].append(next_sequences[idx][-1] + next_sequences[idx+1][-1])
        #print(next_sequences)
        sum += next_sequences[0][-1]
    print(sum)
    
    pass

if __name__=="__main__":
    solve1()
    solve2()


