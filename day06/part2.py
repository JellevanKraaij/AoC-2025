import math

with open("./input.txt", "r") as file:
    lines = file.readlines()

input_lines = [line.strip("\n") for line in lines[:-1]]
instructions_line = lines[-1].strip("\n")

# -------- Calculating column widths --------
widths = []
for c in instructions_line:
	if c in ['+', '*']:
		widths.append(0)
	else:
		widths[-1] += 1

longest = max([len(line) for line in input_lines])
widths[-1] += longest - sum(widths) - len(widths) + 1

# -------- Parsing input based on column widths --------
input = []
for line in input_lines:
	row = []
	for width in widths:
		row.append(line[:width].ljust(width))
		line = line[width + 1:]
	input.append(row)

instructions = instructions_line.strip().split()

# ------- Transposing input --------
input = list(zip(*input))
input = [list(zip(*row)) for row in input]

# ------- Converting character lists to integers --------
input = [[int("".join(x)) for x in row] for row in input]

total = 0
for row, instr in zip(input, instructions):
	if instr == '*':
		total += math.prod(row)
	else:
		total += sum(row)

print(f"total: {total}")
