#!/usr/bin/env python

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
#input = [str.splitlines() for str in test_input.split("\n\n")]

#print(input)

seeds = [int(x.strip()) for x in input[0][0].split(":")[1].split()]
print(seeds)
class Mapper():

    mappings = {}
    reverse_mappings = {}
    mappers = {}
    reverse_mappers = {}
    loaded = []
    def map_from_to(self, source, destination, number, reverse=False):
        key = (source, destination)
        if key in self.mappings:
            return self.direct_map_from_to(source, destination, number, reverse)
        operations = []
        current = destination
        while current != source:
            new_source = self.reverse_mappers[current]
            if not reverse:
                operations.append((new_source, current))
            else:
                operations.append((current, new_source))
            current = new_source
        if not reverse:
            operations.reverse()
        #print(operations)
        for (new_source, new_dest) in operations:
            number = self.direct_map_from_to(new_source, new_dest, number,reverse)
        return number
    def direct_map_from_to(self, source, destination, number, reverse=False):
        mappings = self.mappings
        if reverse:
            mappings = self.reverse_mappings
        ranges = mappings[(source, destination)]
        for (dest_start, source_start, length) in ranges:
            if number >= source_start and number < source_start + length:
                return dest_start + (number  - source_start)
        return number
    def load_mappings(self, array):
        for mapping in array:
            source, dest = mapping[0].split()[0].split("-to-")
            #print(source)
            #print(dest)
            self.mappers[source] = dest
            self.reverse_mappers[dest] = source
            ranges = [[int(str) for str in rang.split()] for rang in mapping[1:]]
            self.mappings[(source, dest)] = ranges
            reverse_ranges = [[arr[1], arr[0], arr[2]] for arr in ranges]
            self.reverse_mappings[(dest, source)] = reverse_ranges
            self.loaded.append(source)
    pass


mapper = Mapper()
mapper.load_mappings(input[1:]) 
def solve1():
    print("-"*25)
    print(" "*9  + "Solve1")
    print("-"*25)
    lowest = -1
    for seed in seeds:
        loc = mapper.map_from_to("seed", "location", seed)
        if loc < lowest or lowest == -1:
            lowest = loc
    print(lowest)

seed_ranges = []
for i in range(0,len(seeds),2):
    #print(i)
    range_start = seeds[i]
    range_length = seeds[i+1]
    seed_ranges += [(range_start, range_length)]
def find(number):
    seed = mapper.map_from_to("seed", "location", number, True)
    for seed_range in seed_ranges:
        if seed >= seed_range[0] and seed < seed_range[0] + seed_range[1]:
            return number
    return None
def solve2():
    print("-"*25)
    print(" "*9  + "Solve2")
    print("-"*25)
    lowest = -1


    res = None

    from multiprocessing import Pool
    results = []
    with Pool() as executor:
        it = executor.imap(find, range(999_999_999_999), chunksize=512)
        count = 0
        for res in it:
            count += 1
            if count % 1_000_000 == 0:
                print(f"{count=}")
            if res:
                results += [res]
                executor.terminate()
                break
    print(min(results))
    return

    for i in range(999_999_999_999):
        res = find(i)
        if res:
            break
    print(res)

if __name__=="__main__":
    solve1()
    solve2()


