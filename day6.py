SIZE = 14

f = open("day6input.txt")
contents = f.read().rstrip()
groups = [
    (index+SIZE, set(contents[index:index+SIZE]))
    for index, character in enumerate(contents)
]
candidates = [
    (index, group)
    for (index, group) in groups
    if len(group) == SIZE
]
print(candidates[0])
