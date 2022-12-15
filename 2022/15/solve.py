#!/usr/bin/env python
from dataclasses import dataclass
from multiprocessing import Pool

@dataclass
class Sensor():
    pos_x : int
    pos_y : int
    
    beacon_x : int
    beacon_y : int
    
    def dist(self):
        return self.dist_to(self.beacon_x, self.beacon_y)
    
    def dist_to(self, x, y):
        return abs(x - self.pos_x) + abs(y - self.pos_y)

def parse_sensor(line):
    sensor, beacon = line.split(":")
    sensor = sensor[sensor.index("x"):]
    s_x, s_y = [int((x[x.index("=")+1:]).strip()) for x in sensor.split(",")]
    beacon = beacon[beacon.index("x"):]
    b_x, b_y = [int((x[x.index("=")+1:]).strip()) for x in beacon.split(",")]
    #print(f"{s_x=} {s_y=} - {b_x=} {b_y=}")
    return Sensor(s_x, s_y, b_x, b_y)

input=[]
with open("input") as f:
    input = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""
    input = f.read().splitlines() # lines without \n

    sensors = []
    for line in input:
        sensors += [parse_sensor(line)]
    print(sensors)
    min_x = min([sensor.pos_x - sensor.dist() for sensor in sensors])
    min_y = min([sensor.pos_y - sensor.dist() for sensor in sensors])
    max_x = max([sensor.pos_x + sensor.dist() for sensor in sensors])
    max_y = max([sensor.pos_y + sensor.dist() for sensor in sensors])
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    print(f"{min_x=} {min_y=} {max_x=} {max_y=} {width=} {height=}")
    

def solve1_failed():
    grid = [["." for x in range(width)] for y in range(height)]
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            y_pos = y + min_y
            x_pos = x + min_x
            for sensor in sensors:
                if sensor.pos_x == x_pos and sensor.pos_y == y_pos:
                    grid[y][x] = "S"
                elif sensor.beacon_x == x_pos and sensor.beacon_y == y_pos:
                    grid[y][x] = "B"
                elif grid[y][x] == "." and sensor.dist_to(x_pos, y_pos) <= sensor.dist():
                    #print(f"{sensor=} {sensor.dist_to(x_pos, y_pos)=} {sensor.dist()=} {x_pos=} {y_pos=} {x=} {y=}")
                    grid[y][x] = "#"
    print("\n".join(["".join(line) for line in grid]))
    total = 0
    y_pos = 2000000 - min_y
    for x in range(len(grid[y_pos])):
        if grid[y_pos][x] == "#" or grid[y_pos][x] == "S":
            total += 1
    print(f"{total=}")
    
def solve1():
    print("-"*25)
    print(" "*9  + "Solve1")
    print("-"*25)
    total = 0
    y = 2000000
    beacon_positions = []
    for sensor in sensors:
        beacon_positions += [(sensor.beacon_x, sensor.beacon_y)]
    for x in range(min_x, max_x+1):
        if x % 100_000 == 0:
            print(x)
        if (x, y) in beacon_positions:
            continue
        for sensor in sensors:
            if sensor.dist_to(x, y) <= sensor.dist():
                total += 1
                break
                
    print(f"{total=}")

def solve2_bruteforce():
    upper = 400000 + 1
    #upper = 20 + 1
    res = 0
    found = False
    beacon_positions = []
    for sensor in sensors:
        beacon_positions += [(sensor.beacon_x, sensor.beacon_y)]
    for y in range(upper):
        if found:
            break
        if y % 100_000 == 0:
            print(f"{y} / {height}")
        for x in range(upper):
            if y % 10000 == 0 and x % 100_000 == 0:
                print(".", end="", flush=True)
            if (x, y) in beacon_positions:
                continue
            possible = True
            for sensor in sensors:
                if sensor.dist_to(x, y) <= sensor.dist():
                    if x == 2 and y == 10:
                        print(f"Failed at {sensor=}")
                    possible = False
                    break
            
            if possible:
                print(f"{x=} {y=}")
                res = x * 4000000 + y
                found = True
                break
        if y % 10000 == 0:
            print()
    print()
    print(f"{res=}")
    
def solve2_failed():
    print("-"*25)
    print(" "*9  + "Solve2")
    print("-"*25)
    upper = 400000
    #upper = 20
    possible_positions = []
    for sensor in sensors:
        dist = sensor.dist() + 1
        for y in range(sensor.pos_y - dist, sensor.pos_y + dist):
            x_mod = dist - sensor.dist_to(sensor.pos_x, y)
            x = sensor.pos_x - x_mod
            if y >= 0 and x >= 0 and y <= upper and x <= upper:
                possible_positions += [(x, y)]
            if x_mod != 0:
                x = sensor.pos_x + x_mod
            if y >= 0 and x >= 0 and y <= upper and x <= upper:
                possible_positions += [(x, y)]
    print(len(possible_positions))
    res = 0
    for pos in possible_positions:
        possible = True
        for sensor in sensors:
            if sensor.dist_to(pos[0], pos[1]) <= sensor.dist() or (sensor.beacon_x == pos[0] and sensor.beacon_y == pos[1]):
                possible = False
                break
        if possible:
            print(f"found: {pos=}")
            #print(f"{(pos[0] * 4000000)=} {pos[1]=} {(pos[0] * 4000000 + pos[1])=}")
            res = pos[0] * 4000000 + pos[1]
            break
    print(f"{res}")
    
def find(dist_mod, center, upper, sensors):
    print(dist_mod)
    found = False
    res = 0
    pos = (0, 0)
    c_dist = center.dist() + dist_mod
    for y in range(center.pos_y - c_dist, center.pos_y + c_dist + 1):
        if found:
            break
        x_mod = c_dist - center.dist_to(center.pos_x, y)
        x = center.pos_x - x_mod
        y_mod = center.pos_y - y
        #print(f"{center=} {y_mod=} {x_mod=}: {y=} {x=}")
        if y >= 0 and x >= 0 and y <= upper and x <= upper:
            possible = True
            for sensor in sensors:
                if sensor.dist_to(x, y) <= sensor.dist() or (sensor.beacon_x == x and sensor.beacon_y == y):
                    possible = False
                    break
            if possible:
                print(f"Found {x=} {y=}")
                found = True
                res = x * 4000000 + y
                break
        if x_mod != 0:
            x = center.pos_x + x_mod
        if y >= 0 and x >= 0 and y <= upper and x <= upper:
            possible = True
            for sensor in sensors:
                if sensor.dist_to(x, y) <= sensor.dist() or (sensor.beacon_x == x and sensor.beacon_y == y):
                    possible = False
                    break
            if possible:
                res = x * 4000000 + y
                pos = (x, y)
                print(f"Found {x=} {y=} {dist_mod=} {res=}")
                found = True
                break
    return (found, res, pos)
    
    
def m_find(tup):
    dist_mod, center, upper, sensors = tup
    return find(dist_mod, center, upper, sensors)
def solve2_slow():
    upper = 4_000_000
    upper = 20
    center_pos = (sum([sensor.pos_x for sensor in sensors]) / len(sensors), sum([sensor.pos_y for sensor in sensors]) / len(sensors))
    c_dist = None
    center = None
    for sensor in sensors:
        if c_dist == None or sensor.dist_to(center_pos[0], center_pos[1]) < c_dist:
            c_dist = sensor.dist_to(center_pos[0], center_pos[1])
            center = sensor
    print(f"{center=} {center_pos=}")
    res = 0
    found = False
    dist = center.dist()
    with Pool() as pool:
        results = pool.imap_unordered(m_find, [(dist_mod, center, upper, sensors) for dist_mod in range(1, upper - dist + 1)], chunksize=250)
        for result in results:
            found, res, pos = result
            if found:
                print(f"{res=} {pos=}")
                pool.close()
                
    
    #for dist_mod in range(1, upper - dist + 1):
    #    found, res = find(dist_mod, center, upper)
    #    if found:
    #        break
    
    
def solve2():
    #nearest neighbors
    upper = 4_000_000
    #upper = 20
    
    for y in range(upper+1):
        if y % 100_000 == 0:
            print(f"{y} / {upper}")
        ranges = []
        for sensor in sensors:
            offset = sensor.dist() - abs(y - sensor.pos_y)
            if offset < 0:
                continue
            ranges += [[sensor.pos_x - offset, sensor.pos_x + offset]]
            
        ranges.sort()
        joined_ranges = []
        found = False
        #print(ranges)
        for r in ranges:
            if len(joined_ranges) == 0:
                joined_ranges += [r]
                continue
            
            #overlap
            r2 = joined_ranges[-1]
            if r[0] <= r2[1] + 1:
                joined_ranges[-1][1] = max(r[1], r2[1])
            else:
                print(f"{r} {r2}")
                found = True
                x = r[0]-1
                print(f"{x=}  {y=} {x*upper + y=}")
                break
        if found:
            break
            
            
    
    

if __name__=="__main__":
    #solve1()
    solve2()


