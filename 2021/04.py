with open('04.in', 'r') as f:
	nums = f.readline()
	f.readline() # omit the empty line right before boards
	boards = f.read()[:-1].split('\n\n')

nums = [int(n) for n in nums.split(',')]

for i in range(len(boards)):
	boards[i] = boards[i].replace('\n',' ').split()
	for j in range(len(boards[i])):
		boards[i][j] = int(boards[i][j])

def mark_num_on_board(num, board):
	for idx, n in enumerate(board):
		if n == num:
			board[idx] = 'X'

def check_columns_for_bingo(board):
	all_column_indexes = [
		[0,5,10,15,20],
		[1,6,11,16,21],
		[2,7,12,17,22],
		[3,8,13,18,23],
		[4,9,14,19,24],
	]

	for single_col_indexes in all_column_indexes:
		curr_col = []
		for idx in single_col_indexes:
			curr_col.append(board[idx])

		if curr_col.count('X') == 5:
			return True

	return False

def check_rows_for_bingo(board):
	all_row_indexes = [
		[0,1,2,3,4],
		[5,6,7,8,9],
		[10,11,12,13,14],
		[15,16,17,18,19],
		[20,21,22,23,24],
	]

	for single_row_indexes in all_row_indexes:
		curr_row = []
		for idx in single_row_indexes:
			curr_row.append(board[idx])

		if curr_row.count('X') == 5:
			return True

	return False

def check_for_bingo(board):
	if check_columns_for_bingo(board) or check_rows_for_bingo(board):
		return True
	else:
		return False

def sum_all_unmarked(board):
	result = 0

	for num in board:
		if num != 'X':
			result += num

	return result

# Part 2
boards_that_won = []
num_of_boards = len(boards)
bingo = False
num_idx = 0
while not bingo:
	for board_idx in range(len(boards)):
		mark_num_on_board(nums[num_idx], boards[board_idx])

	for board_idx, board in enumerate(boards):
		if check_for_bingo(board) and board_idx not in boards_that_won:
			boards_that_won.append(board_idx)
			if len(boards_that_won) == len(boards):
				num1 = sum_all_unmarked(board)
				num2 = nums[num_idx]
				print(f'result is {num1*num2}')
				bingo = True
				break
	num_idx += 1


# # Part 1
# bingo = False
# num_idx = 0
# while not bingo:
	# for board_idx in range(len(boards)):
		# mark_num_on_board(nums[num_idx], boards[board_idx])
		# if check_for_bingo(boards[board_idx]):
			# print(
				# 'current num is',
				# nums[num_idx],
				# '\nsum is',
				# sum_all_unmarked(boards[board_idx]),
				# '\nfinal result is',
				# nums[num_idx] * sum_all_unmarked(boards[board_idx])
				# )
			# bingo = True
	# num_idx += 1
