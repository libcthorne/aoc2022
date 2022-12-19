from functools import reduce

f = open("day5input.txt")

raw_stacks, raw_instructions = f.read().rstrip().split("\n\n")

stacks = list(map(
    lambda stack: list(reversed([x for x in stack if x != ' '])),
    reduce(
        lambda aggr, x: [
            aggr[0]+[x[0]],
            aggr[1]+[x[1]],
            aggr[2]+[x[2]],
            aggr[3]+[x[3]],
            aggr[4]+[x[4]],
            aggr[5]+[x[5]],
            aggr[6]+[x[6]],
            aggr[7]+[x[7]],
            aggr[8]+[x[8]],
        ],
        [
            stack[1::4]
        for index, stack in enumerate(raw_stacks.split("\n"))
        ][:-1],
        [[], [], [], [], [], [], [], [], []],
    )
))

instructions = [
    # count, from_stack, to_stack
    tuple(map(int, raw_instruction.split(" ")[1::2]))
    for raw_instruction in raw_instructions.split("\n")
]

for (count, from_stack, to_stack) in instructions:
    print(stacks)
    print(count, from_stack, to_stack)
    # for _ in range(count):
    #     item = stacks[from_stack-1].pop()
    #     stacks[to_stack-1].append(item)
    #     print(stacks)
    items = []
    for _ in range(count):
        items.append(stacks[from_stack-1].pop())
    for item in reversed(items):
        stacks[to_stack-1].append(item)


for stack in stacks:
    print(stack.pop())
