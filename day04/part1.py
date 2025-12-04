with open("./input.txt", "r") as file:
	grid = [[1 if c == "@" else 0 for c in line.strip()] for line in file.readlines()]

height = len(grid)
width = len(grid[0])

neighbors = [(-1, -1), (-1, 0), (-1, 1),
			 (0, -1),           (0, 1),
			 (1, -1),  (1, 0),  (1, 1)]

def count_neighbors(grid, x, y):
	count = 0
	for dy, dx in neighbors:
		nx, ny = x + dx, y + dy
		if 0 <= nx < width and 0 <= ny < height:
			count += grid[ny][nx]
	return count


accessible = 0
for y in range(height):
	for x in range(width):
		if (grid[y][x] == 1 and count_neighbors(grid, x, y) < 4):
			accessible += 1


print(f"Accessible rolls: {accessible}")