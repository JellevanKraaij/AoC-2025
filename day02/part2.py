import math

def is_repeated(number, size):
	part = str(number)[:size]
	for i in range(size, len(str(number)), size):
		if str(number)[i:i + size] != part:
			return False
	return True

def is_sequence(number):
	for i in range(1, len(str(number)) // 2 + 1):
		if (len(str(number)) % i != 0):
			continue
		if is_repeated(number, i):
			# print(f"Found sequence: {number} (size {i})")
			return True
	return False

with open("input.txt", "r") as file:
    content = file.read().strip()

content = content.replace('\n', '')

pairs = []
for pair in content.split(','):
    pairs.append(pair.split('-'))

invalid_total = 0
for pair in pairs:
	for i in range(int(pair[0]), int(pair[1]) + 1):
		if (is_sequence(i)):
			invalid_total += i

print(f"Final Total: {invalid_total}")
