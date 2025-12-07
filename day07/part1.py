lines = open("./input.txt", "r").readlines()
lines = [list(line.strip("\n")) for line in lines]


def split_beam(line, x):
    for i in (-1, 1):
        line[x + i] = "|"


total = 0
for y in range(1, len(lines)):
    for x in range(len(lines[y])):
        if lines[y - 1][x] in ("S", "|"):
            if lines[y][x] == "^":
                split_beam(lines[y], x)
                total += 1
            else:
                lines[y][x] = "|"


for line in lines:
    print("".join(line))

print(f"Part 1: {total}")
