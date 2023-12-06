#!/usr/bin/env python

from dataclasses import dataclass
import itertools
import numbers

input=[]
with open("input") as f:
    input = [input.splitlines() for input in f.read().split("\n\n")] # lines without \n

test_input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
input = [str.splitlines() for str in test_input.split("\n\n")]

seeds = [int(x.strip()) for x in input[0][0].split(":")[1].split()]

@dataclass
class Range:
    input_start: int
    output_start: int
    length: int

    def __contains__(self, other):
        if isinstance(other, numbers.Number):
            return other >= self.input_start and other < self.input_start + self.length
        return self.input_start <= other.input_start and self.input_start + self.length >= other.input_start + outher.length

    """
    returns a new range with input of the first mapped to the output of the second
    returns None if there is no overlap
    the returned range consists only of the overlapping parts
    """
    def intersection(self, other):
        intersection_start = max(self.output_start, other.input_start)
        intersection_end = min(self.output_start + self.length, other.input_start + other.length)
        if intersection_end < intersection_start:
            return [Range(self.input_start, self.output_start, self.length)]
        offset = intersection_start - self.output_start
        intersection_length = intersection_end - intersection_start + 1
        pre_range = Range(self.input_start, self.output_start, offset)
        intersected_range = Range(self.input_start + offset, other.output_start + offset, intersection_length)
        post_range = Range(self.input_start + self.length - offset, self.output_start + self.length - offset, offset)
        return [pre_range, intersected_range, post_range]

    def convert(self, number):
        offset = number - self.input_start
        return self.output_start + offset


    def combine(self, other):
        own_offset = self.output_start - self.input_start
        other_offset = other.output_start - other.input_start
        if own_offset != other_offset:
            return None
        if self.input_start == other.input_start:
            return self
        min_range = self
        max_range = other
        if other.input_start < self.input_start:
            min_range = other
            max_range = self
        if min_range.input_start + min_range.length >= max_range.input_start:
            offset = max_range.input_start - min_range.input_start
            new_length = offset + max_range.length
            return Range(min_range.input_start, min_range.output_start, new_length)
forward_ranges = []
for mapping in input[2:]:
    source, dest = mapping[0].split()[0].split("-to-")
    ranges = [[int(str) for str in rang.split()] for rang in mapping[1:]] # list of lists with dest_start, source_start, length
    ranges = [Range(rang[0], rang[1], rang[2]) for rang in ranges]
    print(ranges)
    def compact(range_list):
        new_ranges = []
        while len(range_list) > 0:
            combined = range_list.pop()
            next_ranges = []
            for rang2 in range_list:
                new_combined = combined.combine(rang2)
                if new_combined:
                    combined = new_combined
                else:
                    next_ranges.append(rang2)
            new_ranges.append(combined)
            range_list = next_ranges
        return new_ranges
    print(ranges)
    ranges = compact(ranges)
    print(f"{ranges=}")
    if forward_ranges:
        forward_ranges = [y for old_range in forward_ranges for new_range in ranges if (x:=old_range.intersection(new_range)) for y in x if y]
    else:
        forward_ranges = ranges
    forward_ranges = compact(forward_ranges)
    print(f"{forward_ranges=}")
    print(len(forward_ranges))


def solve1():
    print("-"*25)
    print(" "*9  + "Solve1")
    print("-"*25)
    def find_range(number):
        for rang in forward_ranges:
            if number in rang:
                return rang
        return Range(number, number, 1)
    
    print(min([find_range(seed).convert(seed) for seed in seeds]))
    pass

def solve2():
    print("-"*25)
    print(" "*9  + "Solve2")
    print("-"*25)
    
    pass

if __name__=="__main__":
    solve1()
    solve2()


