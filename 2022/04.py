with open('04.in', 'r') as f:
	raw_pairs = [rp.strip().replace('-', ',').split(',') for rp in f.readlines()]

def part1():
	count = 0
	for pair in raw_pairs:
		pair = [int(digit) for digit in pair]
		
		cond1 = pair[0] <= pair[2] and pair[1] >= pair[3]
		cond2 = pair[0] >= pair[2] and pair[1] <= pair[3]
		
		if cond1 or cond2:
			count += 1
			
	print(count)

def part2():
	count = 0
	for pair in raw_pairs:
		pair = [int(digit) for digit in pair]
		
		if pair[2] > pair[1] or pair[3] < pair[0]:
			count += 1
			
	print(len(raw_pairs) - count)
