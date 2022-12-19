f = open("day9input.txt")
contents = f.read().rstrip().split("\n")
instructions = [line.split(" ") for line in contents]
instructions = [(direction, int(amount)) for (direction, amount) in instructions]

knots = [
    (0, 0)
    for _ in range(10)
]
tail_positions = set()

for (direction, amount) in instructions:
    for _ in range(amount):
        if direction == "R":
            knots[0] = (knots[0][0]+1, knots[0][1])
        elif direction == "L":
            knots[0] = (knots[0][0]-1, knots[0][1])
        elif direction == "U":
            knots[0] = (knots[0][0], knots[0][1]-1)
        elif direction == "D":
            knots[0] = (knots[0][0], knots[0][1]+1)

        for parent_index in range(len(knots)-1):
            child_index = parent_index + 1

            x_distance = abs(knots[child_index][0] - knots[parent_index][0])
            x_delta = -1 if knots[child_index][0] - knots[parent_index][0] > 0 else 1
            y_distance = abs(knots[child_index][1] - knots[parent_index][1])
            y_delta = -1 if knots[child_index][1] - knots[parent_index][1] > 0 else 1

            if x_distance > 1 and y_distance > 1:
                knots[child_index] = (knots[child_index][0]+x_delta, knots[child_index][1]+y_delta)
            elif x_distance > 1:
                knots[child_index] = (knots[child_index][0]+x_delta, knots[parent_index][1])
            elif y_distance > 1:
                knots[child_index] = (knots[parent_index][0], knots[child_index][1]+y_delta)

            if child_index == len(knots)-1:
                tail_positions.add(knots[child_index])

print(len(tail_positions))
