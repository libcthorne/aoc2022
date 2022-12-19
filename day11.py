from math import prod
from pprint import pprint


f = open("day11input.txt")
contents = f.read().rstrip().split("\n")

monkeys = {}
monkey_number = None
for line in contents:
    if line.endswith(":"):
        monkey_number = int(line.split(" ")[1][:-1])
        monkeys[monkey_number] = {"inspect_count": 0}
    elif "Starting items:" in line:
        item_worry_levels = list(map(int, line.split(": ")[1].split(", ")))
        monkeys[monkey_number]["item_worry_levels"] = item_worry_levels
    elif "Operation:" in line:
        operation = line.split(": ")[1]
        monkeys[monkey_number]["operation"] = operation
    elif "Test:" in line:
        division_test = int(line.split("divisible by ")[1])
        monkeys[monkey_number]["division_test"] = division_test
    elif "If true:" in line:
        true_monkey = int(line.split("to monkey ")[1])
        monkeys[monkey_number]["true_monkey"] = true_monkey
    elif "If false:" in line:
        false_monkey = int(line.split("to monkey ")[1])
        monkeys[monkey_number]["false_monkey"] = false_monkey


max_divisor = prod(monkey["division_test"] for monkey in monkeys.values())

pprint(monkeys)

for round_number in range(10000):
    print(round_number)
    for monkey_number, monkey in monkeys.items():
        #print(f"Monkey {monkey_number}:")
        for worry_level in monkey["item_worry_levels"]:
            monkey["inspect_count"] += 1
            #print(f"Monkey inspects an item with worry level of {worry_level}")
            old = worry_level
            exec(monkey["operation"])
            #print(f"Worry level is now {new}")
            #new //= 3
            new = new % max_divisor
            #print(f"Monkey got bored, worry level is now {new}")
            division_test = monkey["division_test"]
            remainder = new % division_test
            next_level = new
            if remainder == 0:
                #print(f"Current worry level is divisible by {division_test}.")
                monkeys[monkey["true_monkey"]]["item_worry_levels"].append(next_level)
            else:
                #print(f"Current worry level is not divisible by {division_test}.")
                monkeys[monkey["false_monkey"]]["item_worry_levels"].append(next_level)
            #print("\n")
        monkey["item_worry_levels"] = []
        #print("\n")

ranked_monkeys = sorted(list(monkeys.values()), key=lambda monkey: monkey["inspect_count"], reverse=True)
busiest_monkeys = ranked_monkeys[:2]

print(busiest_monkeys[0]["inspect_count"] * busiest_monkeys[1]["inspect_count"])
