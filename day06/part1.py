with open("./input.txt", "r") as file:
    lines = file.readlines()

table = []

data = lines[:-1]  # Exclude the last line
instructions = lines[-1].strip().split()

for line in data:
    row = line.strip().split()
    table.append([int(x) for x in row])

table = list(zip(*table))

total = 0
for i, instr in enumerate(instructions):
	result = 1 if instr == '*' else 0
	for num in table[i]:
		if instr == '*':
			result *= num
		else:
			result += num
	total += result

print(f"total: {total}")