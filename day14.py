import math
import sys

f = open("day14input.txt")
contents = f.read().rstrip().split("\n")
rocks = [
    [
        list(map(int, coordinates.split(",")))
        for coordinates in line.split(" -> ")
    ]
    for line in contents
]

SAND_POS = (500, 0)

grid = {
    SAND_POS: "+",
}

min_x = 500
max_x = -math.inf
min_y = 0
max_y = -math.inf

for rock in rocks:
    print("Rock")
    for index in range(len(rock)-1):
        start = rock[index]
        end = rock[index+1]

        min_x = min(min_x, start[0], end[0])
        max_x = max(max_x, start[0], end[0])
        min_y = min(min_y, start[1], end[1])
        max_y = max(max_y, start[1], end[1])

        if start[0] > end[0]:
            print("<-")
            y = start[1]
            for x in range(end[0], start[0]+1):
                print(x,y)
                grid[(x, y)] = "#"
        elif end[0] > start[0]:
            print("->")
            y = start[1]
            for x in range(start[0], end[0]+1):
                print(x,y)
                grid[(x, y)] = "#"
        elif start[1] > end[1]:
            print("^")
            x = start[0]
            for y in range(end[1], start[1]+1):
                print(x,y)
                grid[(x, y)] = "#"
        elif end[1] > start[1]:
            print("v")
            x = start[0]
            for y in range(start[1], end[1]+1):
                print(x,y)
                grid[(x, y)] = "#"


for x in range(-1000, 1000):
    grid[(x, max_y+2)] = "#"


def print_grid():
    for y in range(min_y-1, max_y+4):
        for x in range(min_x-30, max_x+30):
            pos = (x, y)
            sys.stdout.write(grid.get(pos, "."))
        sys.stdout.write("\n")


print_grid()


def add_sand(grain_number):
    previous = None
    pos = (SAND_POS[0], SAND_POS[1])
    while True:
        # if (
        #     pos[0] < min_x
        #     or pos[0] > max_x
        #     or pos[1] > max_y
        # ):
        #     print(f"Grain {grain_number}: OOL")
        #     return False

        if previous in grid:
            del grid[previous]
        previous = pos
        moved = False
        for pos_option in (
            (pos[0], pos[1]+1),
            (pos[0]-1, pos[1]+1),
            (pos[0]+1, pos[1]+1),
        ):
            entity = grid.get(pos_option, ".")
            if entity == ".":
                pos = pos_option
                grid[pos] = "o"
                moved = True
                break
            elif entity in ("o", "#"):
                continue
        if not moved:
            break

    if pos == SAND_POS:
        print(f"Grain {grain_number}: Full")
        return False

    return True


grain_number = 0
while True:
    grain_number += 1
    if not add_sand(grain_number):
        break

print_grid()
