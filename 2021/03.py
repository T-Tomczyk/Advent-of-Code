# Took 1:10 to solve on 2021-12-03

### Input
with open('03.in', 'r') as f:
	inp = [l.strip() for l in f.readlines()]

### Part 2
import copy

def num_of_1s_in_column(inp, col_idx):
	result = 0

	for num in inp:
		if num[col_idx] == '1':
			result += 1

	return result

def most_common_in_column(inp, col_idx):
	num_of_nums = len(inp)
	num_of_1s = num_of_1s_in_column(inp, col_idx)
	num_of_0s = num_of_nums - num_of_1s

	if num_of_1s >= num_of_0s:
		return '1'
	else:
		return '0'

def filter_inp(inp, leave_most_common):
	filtered = copy.deepcopy(inp)

	col_idx = 0
	while len(filtered) > 1:
		num_of_1s = num_of_1s_in_column(filtered, col_idx)
		most_common = most_common_in_column(filtered, col_idx)

		num_idx = 0
		while num_idx < len(filtered):
			if (leave_most_common and
			filtered[num_idx][col_idx] != most_common) or (
			not leave_most_common and
			filtered[num_idx][col_idx] == most_common):
				del filtered[num_idx]
				num_idx -= 1
			num_idx += 1

		col_idx += 1

	return filtered

oxygen = filter_inp(inp, True)
scrubber = filter_inp(inp, False)
life = int(oxygen[0], 2) * int(scrubber[0], 2)
print(life)




### Part 1

# # count how many 1's in each column
# count_of_1s = [0]*len(inp[1])
# for num in inp:
	# for idx, bit in enumerate(num):
		# if bit == '1':
			# count_of_1s[idx] += 1

# # assume 0 most common for every column and change to 1 if so
# most_common = ['0']*len(inp[1])
# half_of_column = len(inp)/2
# for idx, count in enumerate(count_of_1s):
	# if count > half_of_column:
		# most_common[idx] = '1'

# # convert most_common to least_common
# least_common = []
# for bit in most_common:
	# if bit == '1':
		# least_common.append('0')
	# else:
		# least_common.append('1')

# gamma_rate = int(''.join(most_common), 2)
# epsilon_rate = int(''.join(least_common), 2)

# print('power consumption:', gamma_rate * epsilon_rate)
