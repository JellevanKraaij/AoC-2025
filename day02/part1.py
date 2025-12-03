with open("input.txt", "r") as file:
    content = file.read().strip()

pairs = []
for pair in content.split(','):
    pairs.append(pair.split('-'))

invalid_total = 0
for pair in pairs:
	for i in range(int(pair[0]), int(pair[1]) + 1):
		str_i = str(i)
		if len(str_i) % 2 != 0:
			continue
		left = str_i[:len(str_i)//2]
		right = str_i[len(str_i)//2:]
		# print(f"Checking pair: {pair} => {i} ({left} vs {right})")
		if (left == right):
			# print(f"Found matching pair: {pair} => {i} ({left} vs {right})")
			invalid_total += i

print(f"Final Total: {invalid_total}")
