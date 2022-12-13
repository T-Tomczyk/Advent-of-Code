with open('11.in') as f:
	monkeys = [m.strip() for m in f.read().split('\n\n')]

# Input parsing.
for i in range(len(monkeys)):
	monkeys[i] = monkeys[i].split('\n')
	for j in range(len(monkeys[i])):
		monkeys[i][j] = monkeys[i][j].strip()

monkey_dict = {}

for m in monkeys:

	m_idx = int(m[0].replace('Monkey ', '').replace(':', '').strip())
	items = [int(i) for i in m[1].replace('Starting items: ', '').split(', ')]
	op = m[2].replace('Operation: new = ','')
	divisible_by = int(m[3].split()[-1])
	if_true = int(m[4].split()[-1])
	if_false = int(m[5].split()[-1])

	monkey_dict[m_idx] = {
		'items': items,
		'op': op,
		'divisible_by': divisible_by,
		'if_true': if_true,
		'if_false': if_false
	}

# Logic.
def modify_worry_level(old, op):
	num1, sign, num2 = op.strip().split()

	if num1 == 'old':
		num1 = old

	if num2 == 'old':
		num2 = old
		
	num1 = int(num1)
	num2 = int(num2)

	if sign == '+':
		return num1 + num2
	elif sign == '*':
		return num1 * num2


num_of_rounds = 20
inspections = {}
for _ in range(num_of_rounds):

	for monkey_idx, desc in monkey_dict.items():
			
		op = desc['op']
		divisible_by = desc['divisible_by']
		if_true = desc['if_true']
		if_false = desc['if_false']

		while len(monkey_dict[monkey_idx]['items']) > 0:
			
			if monkey_idx in inspections.keys():
				inspections[monkey_idx] += 1
			else:
				inspections[monkey_idx] = 1
			
			starting_worry = monkey_dict[monkey_idx]['items'][0]
			
			# First adjustment.
			monkey_dict[monkey_idx]['items'][0] = modify_worry_level(starting_worry, op)

			# Second adjustment.
			monkey_dict[monkey_idx]['items'][0] //= 3

			# Perform the test and copy the item over to the other monkey.
			if monkey_dict[monkey_idx]['items'][0] % divisible_by == 0:
				monkey_dict[if_true]['items'].append(monkey_dict[monkey_idx]['items'][0])
			else:
				monkey_dict[if_false]['items'].append(monkey_dict[monkey_idx]['items'][0])

			# Remove the item from current monkey.
			del monkey_dict[monkey_idx]['items'][0]

total_inspections = [i for i in inspections.values()]
total_inspections.sort()
print(total_inspections[-1] * total_inspections[-2])
