import string
from collections import Counter

# f = open("day3input.txt")
# rucksacks = sum([
#     string.ascii_letters.find((set(contents[:len(contents)//2]) & set(contents[len(contents)//2:])).pop()) + 1
#     for contents in f.read().strip().split("\n")
# ])
# print(len(rucksacks))

f = open("day3input.txt")
lines = f.read().strip().split("\n")
rucksacks = sum([
    string.ascii_letters.find((set(lines[i]) & set(lines[i+1]) & set(lines[i+2])).pop()) + 1
    for i, contents in enumerate(lines)
    if i % 3 == 0
])
print(rucksacks)
