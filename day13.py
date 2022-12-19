import ast
import functools
from pprint import pprint


f = open("day13input.txt")
# pair_lines = f.read().rstrip().split("\n\n")
# pairs = [
#     [ast.literal_eval(s) for s in pair_line.split("\n")]
#     for pair_line in pair_lines
# ]
contents = f.read().rstrip().replace("\n\n", "\n").split("\n")
packets = [
    [ast.literal_eval(s) for s in line.split("\n")]
    for line in contents
]
packets.append([[2]])
packets.append([[6]])


def is_ordered(lhs, rhs):
    checks = [
        (lhs, rhs),
    ]

    while checks:
        check_lhs, check_rhs = checks.pop(0)

        #print(f"is_ordered({check_lhs}, {check_rhs})")
        if isinstance(check_lhs, int) and isinstance(check_rhs, int):
            if check_lhs < check_rhs:
                return -1
            elif check_lhs > check_rhs:
                return 1
            else:
                continue
        elif isinstance(check_lhs, int) and isinstance(check_rhs, list):
            check_lhs = [check_lhs]
        elif isinstance(check_rhs, int) and isinstance(check_lhs, list):
            check_rhs = [check_rhs]

        if len(check_lhs) == 0 and len(check_rhs) == 0:
            continue
        if len(check_lhs) == 0:
            return -1
        if len(check_rhs) == 0:
            return 1

        checks = [
            (check_lhs[0], check_rhs[0]),
            (check_lhs[1:], check_rhs[1:]),
        ] + checks

    return 0


# pair_indices_sum = 0
# for pair_index, pair in enumerate(pairs):
#     print("-" * 80)
#     print(f"Pair {pair_index+1}")
#     print("-" * 80)
#     lhs, rhs = pair
#     if is_ordered(lhs, rhs):
#         print("Ordered")
#         pair_indices_sum += (pair_index+1)
#     else:
#         print("Not ordered")

result = sorted(packets, key=functools.cmp_to_key(is_ordered))
pprint(result)
a = (result.index([[2]])+1) * (result.index([[6]])+1)
print(a)

#print(pair_indices_sum)
