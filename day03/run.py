with open("./input.txt", "r") as file:
    lines = file.readlines()

def find_largest_with_room(line, room):
    for i in reversed(range(1,10)):
        first = line.find(str(i))
        if first < 0:
            continue
        if len(line) - first > room:
            return first
    return 0

def find_highest_power(line, amount):
    res = ""
    for i in reversed(range(0, amount)):
        pos = find_largest_with_room(line, i)
        res += str(line[pos])
        line = line[pos + 1:]
    return int(res)

total1 = 0
total2 = 0

for line in lines:
    line = line.strip()
    total1 += find_highest_power(line, 2)
    total2 += find_highest_power(line, 12)

print(f"Part 1 Total Power: {total1}")
print(f"Part 2 Total Power: {total2}")