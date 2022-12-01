with open('02.in', 'r') as f:
	inp = [l.strip() for l in f.readlines()]


### Part 2

fwd = 0
dep = 0
aim = 0

for instruction in inp:
	direction, value = instruction.split()
	value = int(value)

	if direction == 'forward':
		fwd += value
		dep += value * aim
	elif direction == 'down':
		aim += value
	elif direction == 'up':
		aim -= value

print(fwd, dep, fwd*dep)




### Part 1

# fwd = 0
# dep = 0

# for instruction in inp:
	# direction, value = instruction.split()
	# value = int(value)

	# if direction == 'forward':
		# fwd += value
	# elif direction == 'down':
		# dep += value
	# elif direction == 'up':
		# dep -= value

# print(fwd, dep, fwd*dep)
