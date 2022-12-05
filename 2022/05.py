# Typed manually based on the first part of the input.
crates = {
	1: ['D','M','S','Z','R','F','W','N'],
	2: ['W','P','Q','G','S'],
	3: ['W','R','V','Q','F','N','J','C'],
	4: ['F','Z','P','C','G','D','L'],
	5: ['T','P','S'],
	6: ['H','D','F','W','R','L'],
	7: ['Z','N','D','C'],
	8: ['W','N','R','F','V','S','J','Q'],
	9: ['R','M','S','G','Z','W','V'],
}

# Read the second part of the input.
with open('05.in', 'r') as f:
	raw_in = [line.strip().replace('move ', '').replace('from ', '').replace('to ', '') for line in f.readlines()]

# Convert list of strings to a list of lists of integers.
pretty_in = []
for inst in raw_in:
	a,b,c = inst.split(' ')
	pretty_in.append([int(a), int(b), int(c)])
	
def part1():
	for inst in pretty_in:
		number_of_moves = inst[0]
		start = inst[1]
		end = inst[2]
		
		for _ in range(number_of_moves):
			crates[end].append(crates[start].pop())
			
def part2():
	for inst in pretty_in:
		number_of_moves = inst[0]
		start = inst[1]
		end = inst[2]
		
		crates_picked_up = crates[start][-number_of_moves:]
		crates[start] = crates[start][:-number_of_moves]
		crates[end] = crates[end] + crates_picked_up

# ~ part1()
part2()

ans = ''
for crate in crates.values():
	ans += crate[-1]
print(ans)

	
