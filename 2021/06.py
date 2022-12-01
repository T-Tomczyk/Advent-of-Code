with open('06.in', 'r') as f:
	inp = [int(fish) for fish in f.read().split(',')]

def total_offspring(inp, target_day):
	all_fish = {
		0: 0,
		1: 0,
		2: 0,
		3: 0,
		4: 0,
		5: 0,
		6: 0,
		7: 0,
		8: 0
	}

	for fish in inp:
		all_fish[fish] += 1

	for current_day in range(0, target_day):
		new_fish_next_day = all_fish[0]

		for fish_type in range(1, 9):
			all_fish[fish_type-1] = all_fish[fish_type]

		all_fish[6] += new_fish_next_day
		all_fish[8] = new_fish_next_day

	total = 0
	for fish_count in all_fish.values():
		total += fish_count
	return total

print(total_offspring(inp, 256))
