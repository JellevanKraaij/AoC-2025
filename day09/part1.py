from itertools import combinations

lines = open("input.txt").readlines()

tiles = [tuple(int(x) for x in line.strip().split(",")) for line in lines]

combinations = combinations(tiles, 2)

surfaces = []

for (x1, y1), (x2, y2) in combinations:
	length_x = max(x1, x2) - min(x1, x2) + 1
	length_y = max(y1, y2) - min(y1, y2) + 1
	surface = length_x * length_y
	surfaces.append(surface)

print(f"biggest rectangle: {max(surfaces)}")