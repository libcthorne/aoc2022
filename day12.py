import string
from pprint import pprint


f = open("day12input.txt")
contents = f.read().rstrip().split("\n")

grid = {}
grid_neighbours = {}
start = None
end = None

for y, line in enumerate(contents):
    for x, height in enumerate(line):
        position = (x, y)
        if height == "S":
            start = position
            height = "a"
        elif height == "E":
            end = position
            height = "z"
        grid[position] = string.ascii_letters.find(height)


# part 2
start = end


# def find_neighbours(position):
#     my_height = grid[position]
#     up = (position[0], position[1]-1)
#     down = (position[0], position[1]+1)
#     left = (position[0]-1, position[1])
#     right = (position[0]+1, position[1])
#     neighbours = []
#     if up in grid and grid[up] - my_height <= 1:
#         neighbours.append(up)
#     if down in grid and grid[down] - my_height <= 1:
#         neighbours.append(down)
#     if left in grid and grid[left] - my_height <= 1:
#         neighbours.append(left)
#     if right in grid and grid[right] - my_height <= 1:
#         neighbours.append(right)
#     return neighbours


# part 2
def find_neighbours(position):
    my_height = grid[position]
    up = (position[0], position[1]-1)
    down = (position[0], position[1]+1)
    left = (position[0]-1, position[1])
    right = (position[0]+1, position[1])
    neighbours = []
    if up in grid and my_height - grid[up] <= 1:
        neighbours.append(up)
    if down in grid and my_height - grid[down] <= 1:
        neighbours.append(down)
    if left in grid and my_height - grid[left] <= 1:
        neighbours.append(left)
    if right in grid and my_height - grid[right] <= 1:
        neighbours.append(right)
    return neighbours


for position in grid.keys():
    grid_neighbours[position] = find_neighbours(position)


paths = [
    (
        {start}, # seen
        [start], # nodes
    ),
]
scores = {start: 0}
solutions = []

while paths:
    seen, nodes = paths.pop()
    current = nodes[-1]
    neighbours = grid_neighbours[current]
    for neighbour in neighbours:
        #if neighbour == end:
        if grid[neighbour] == 0:
            solution = nodes + [neighbour]
            solutions.append(solution)
        elif neighbour not in seen:
            score = len(nodes)
            if neighbour not in scores or score < scores[neighbour]:
                scores[neighbour] = score
                paths.append(
                    (
                        seen | {neighbour},
                        nodes + [neighbour],
                    )
                )

shortest = sorted(solutions, key=lambda solution: len(solution))[0]
print(len(shortest)-1)
