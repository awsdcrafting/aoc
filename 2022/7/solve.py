#!/usr/bin/env python

class File():
    
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size

class Directory():
    
    def __init__(self, parent, name) -> None:
        self.name = name
        self.parent = parent
        self.files = []
        self.sub_dirs = {}
        self.total_size = 0
        
    def add_file(self, file):
        self.files += [file]
        self.total_size += file.size
        
    def add_dir(self, name):
        if name in self.sub_dirs:
            return
        directory = Directory(self, name)
        self.sub_dirs[name] = directory
        return directory
        
    def get_size(self, dirs=False):
        size = self.total_size
        if dirs:
            for directory in self.sub_dirs.values():
               size += directory.get_size(dirs)
        return size
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.__str__()


input=[]
with open("input") as f:
    input = f.read().splitlines()[1:] # lines without \n #ignore cd into root

root_dir = Directory(None, "/")

current_dir = root_dir

for line in input:
    if line.startswith("$"):
        line = line[2:].strip()
        if line == "ls":
            pass
        elif line.startswith("cd"):
            arg = line[3:]
            if arg == "..":
                current_dir = current_dir.parent
            else:
                if arg in current_dir.sub_dirs:
                    current_dir = current_dir.sub_dirs[arg]
                else:
                    current_dir = current_dir.add_dir(arg)
    elif line.startswith("dir"):
        current_dir.add_dir(line[4:].strip())
    else:
        size, name = line.split(" ")
        current_dir.add_file(File(name, int(size)))
        
        
def find_directories(directory, max_size):
    total = 0
    size = directory.get_size(True)
    if size <= max_size:
        total += size
    for sub_dir in directory.sub_dirs.values():
        total += find_directories(sub_dir, max_size)
    return total

def solve1():
    max_size = 100_000
    total_sum = find_directories(root_dir, max_size)
    print(f"{total_sum=}")



def solve2():
    total_space = 70_000_000
    needed_free = 30_000_000
    used = root_dir.get_size(True)
    current_free = total_space - used
    target = needed_free - current_free
    
    smallest_size = root_dir.get_size(True)
    smallest_dir = root_dir
    list_of_dirs = [root_dir]
    while len(list_of_dirs) > 0:
        directory = list_of_dirs.pop(0)
        dir_size = directory.get_size(True)
        if dir_size >= target:
            list_of_dirs += list(directory.sub_dirs.values())
            if dir_size < smallest_size:
                smallest_dir = directory
                smallest_size = dir_size
    print(f"{smallest_size=}")
    print(f"{smallest_dir.name}")

if __name__=="__main__":
    solve1()
    solve2()


