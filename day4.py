f = open("day4input.txt")

assignments = list(
    filter(
        lambda x: (
            (
                x[0][0] <= x[1][0]
                and x[0][1] >= x[1][1]
            )
            or (
                x[1][0] <= x[0][0]
                and x[1][1] >= x[0][1]
            ) or (
                # ...
                #   ...
                x[0][0] <= x[1][0]
                and x[0][1] >= x[1][0]
            ) or (
                #   ...
                # ...
                x[0][0] <= x[1][1]
                and x[0][1] >= x[1][1]
            )
        ),
        [
            [
                tuple(map(int, assignment.split("-")))
                for assignment in assignments.split(",")
            ]
            for line in f.read().strip().split("\n")
            for assignments in line.split("\n")
        ]
    )
)
print(len(assignments))
