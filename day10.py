import sys

f = open("day10input.txt")
contents = f.read().rstrip().split("\n")

cycle_number = 0
signal_sum = 0
x = 1

image = ""

for instruction in contents:
    if instruction == "noop":
        image += "#" if abs((cycle_number % 40) - x) <= 1 else "."
        cycle_number += 1
        if (cycle_number - 20) % 40 == 0:
            signal_sum += cycle_number * x
    else:
        add_value = int(instruction.split("addx ")[1])

        image += "#" if abs((cycle_number % 40) - x) <= 1 else "."
        cycle_number += 1
        if (cycle_number - 20) % 40 == 0:
            signal_sum += cycle_number * x

        image += "#" if abs((cycle_number % 40) - x) <= 1 else "."
        cycle_number += 1
        if (cycle_number - 20) % 40 == 0:
            signal_sum += cycle_number * x

        x += add_value

#print(signal_sum)
for i, pixel in enumerate(image):
    if i % 40 == 0:
        sys.stdout.write("\n")
    sys.stdout.write(pixel)
sys.stdout.write("\n")
