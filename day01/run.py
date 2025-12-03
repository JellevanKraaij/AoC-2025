with open("./input.txt", "r") as file:
    lines = file.readlines()

position = 50
password1 = 0
password2 = 0

for line in lines:
	operation = line[:1]
	number = int(line[1:])

	for _ in range(number):
		if operation == "L":
			position -= 1
		elif operation == "R":
			position += 1
		position %= 100

		if (position == 0):
			password2 += 1

	if position == 0:
		password1 += 1

	print(f"{operation}{number} => {position}: {password1}, {password2}")

print(f"Part 1 Final Password: {password1}")
print(f"Part 2 Final Password: {password2}")