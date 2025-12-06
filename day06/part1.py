import math

with open("./input.txt", "r") as file:
    lines = file.readlines()

table = []

data = lines[:-1]
instructions = lines[-1].strip().split()

for line in data:
    row = line.strip().split()
    table.append([int(x) for x in row])

table = list(zip(*table))

total = 0
for row, instr in zip(table, instructions):
	if instr == '*':
		total += math.prod(row)
	else:
		total += sum(row)

print(f"total: {total}")