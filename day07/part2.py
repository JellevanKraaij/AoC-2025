import time

lines = open("./input.txt", "r").readlines()
lines = [list(line.strip("\n")) for line in lines]


def print_state(lines):
    for line in lines:
        for c in line:
            if type(c) is int and len(str(c)) != 1:
                c = "^"
            print(c, end="")
        print()


def solve(lines, y, x):
    for i in range(y, len(lines)):
        if lines[i][x] == "^":
            lines[i][x] = solve(lines, i, x - 1) + solve(lines, i, x + 1)
        if type(lines[i][x]) is int:
            return lines[i][x]
        lines[i][x] = "|"
    return 1


total_routes = solve(lines, 1, lines[0].index("S"))

print("Final state:")
print_state(lines)
print()

print(f"Part 2: {total_routes}")