import functools
import itertools
from math import prod
from pprint import pprint


f = open("day8input.txt")
raw_rows = [
    [
        ((column_index, row_index), int(value))
        for column_index, value in enumerate(row)
    ]
    for row_index, row in enumerate(f.read().rstrip().split("\n"))
]

grid = {
    position: value
    for row in raw_rows
    for (position, value) in row
}
grid_width = len(raw_rows[0])
grid_height = len(raw_rows)

rows = list(raw_rows)
rows.extend([list(reversed(row)) for row in rows])
top_to_bottom = [
    [
        raw_rows[row][column]
        for row in range(len(raw_rows))
    ]
    for column in range(len(raw_rows[0]))
]
rows.extend(top_to_bottom)
rows.extend([list(reversed(row)) for row in top_to_bottom])

result = {
    tree
    for row in rows
    for tree in (
        functools.reduce(
            lambda state, value: {
                "threshold": max(state["threshold"], value[1]),
                "trees": state["trees"] + [value[0]] if value[1] > state["threshold"] else state["trees"],
            },
            row,
            {
                "threshold": -1,
                "trees": [],
            },
        )["trees"]
    )
}

#print(sorted(result))
#print(len(result))

scores = [
    prod([
        functools.reduce(
            lambda state, value: {
                "blocked": state["blocked"] or value >= grid[position],
                "count": state["count"] + 1 if not state["blocked"] else state["count"],
            },
            adjacent_trees,
            {
                "blocked": False,
                "count": 0,
            },
        )["count"]
        for adjacent_trees in (
            # up
            [
                grid[(position[0], y)]
                for y in range(position[1]-1, -1, -1)
            ],
            # left
            [
                grid[(x, position[1])]
                for x in range(position[0]-1, -1, -1)
            ],
            # down
            [
                grid[(position[0], y)]
                for y in range(position[1]+1, grid_height)
            ],
            # right
            [
                grid[(x, position[1])]
                for x in range(position[0]+1, grid_width)
            ],
        )
    ])
    for position in grid.keys()
]

#pprint(scores)
pprint(max(scores))
