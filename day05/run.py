with open("./input.txt", "r") as file:
    lines = file.readlines()

blank_line = lines.index("\n")

# ------- Parse input into list of ranges -----------
fresh_ids = []
for line in lines[:blank_line]:
    start, end = line.strip().split("-")
    fresh_ids.append(tuple([int(start), int(end)]))

# -------- Merge ranges ------------

fresh_ids.sort()
i = 0
while i + 1 < len(fresh_ids):
    start, end = fresh_ids[i]
    start1, end1 = fresh_ids[i + 1]

    if start1 <= end + 1:
        fresh_ids[i + 1] = (start, max(end, end1))
        fresh_ids.pop(i)
    else:
        i += 1


# -------- Solve part 1 ------------

total_fresh = 0
for line in lines[blank_line + 1 :]:
    id = int(line.strip())
    for start, end in fresh_ids:
        if start <= id <= end:
            total_fresh += 1
            break

print(f"Total available fresh IDs (part 1): {total_fresh}")

# -------- Solve part 2 ------------

total_fresh = 0
for start, end in fresh_ids:
    total_fresh += end + 1 - start

print(f"Total available fresh IDs (part 2): {total_fresh}")
