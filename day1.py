# f = open("day1input.txt")
# print(max([
#     sum(map(int, group.split("\n")))
#     for group in f.read().strip().split("\n\n")
# ]))

f = open("day1input.txt")
print(sum(sorted([
    sum(map(int, group.split("\n")))
    for group in f.read().strip().split("\n\n")
])[-3:]))
