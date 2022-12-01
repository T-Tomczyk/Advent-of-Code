with open('01.in', 'r') as f:
	lines = f.readlines()

calorie_sums = []
curr_elf_cal = 0

for line in lines:
	if line == '\n':
		calorie_sums.append(curr_elf_cal)
		curr_elf_cal = 0
		continue

	curr_elf_cal += int(line[:-1])

# Part 1
print(max(calorie_sums))

# Part 2
calorie_sums.sort()
print(sum(calorie_sums[-3:]))
