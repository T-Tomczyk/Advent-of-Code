small_input = [
	199,
	200,
	208,
	210,
	200,
	207,
	240,
	269,
	260,
	263,
]

with open('01.in', 'r') as f:
	big_input = [int(l.replace('\n','')) for l in f.readlines()]

def task1(_input):
	increases = 0

	for i, j in enumerate(_input):
		if i == 0:
			continue

		if _input[i] > _input[i-1]:
			increases += 1

	print(increases)

def task2(_input):
	new_input = []

	for i, j in enumerate(_input):
		if i in (0, 1):
			continue

		new_input.append(_input[i] + _input[i-1] + _input[i-2])

	return(new_input)

# task1(big_input)
# task1(task2(big_input))
