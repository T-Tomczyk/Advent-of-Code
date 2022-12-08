with open('08.in', 'r') as f:
	grid = [list(row) for row in [l.strip() for l in f.readlines()]]

dim = len(grid)



# ---------------------- Part 1	

# Convert strings to integers.
for r_idx in range(dim):
	for t_idx, tree in enumerate(grid[r_idx]):
		grid[r_idx][t_idx] = int(tree)
		
# Create a rotated copy of the grid.
rotated_grid = []
for tree_idx in range(dim):
	column = []
	for row_idx in range(dim):
		column.append(grid[row_idx][tree_idx])
	rotated_grid.append(column)
	
# Create a grid of visibilities.
visibilities = [[False for _ in range(dim)] for _ in range(dim)]

# Check if given tree is visible in the given list.
def is_visible(given_tree_idx, tree_list):
	
	# First and last trees are always visible.
	if given_tree_idx == 0 or given_tree_idx == len(tree_list)-1:
		return True

	tree_height = tree_list[given_tree_idx]
	v_from_left = True
	v_from_right = True
	
	# Go from the left.
	for tree_idx in range(given_tree_idx):
		if tree_list[tree_idx] >= tree_height:
			v_from_left = False
			
	# Go from the right.
	for tree_idx in range(len(tree_list)-1, given_tree_idx, -1):
		if tree_list[tree_idx] >= tree_height:
			v_from_right = False
			
	return v_from_left or v_from_right

# Iterate through the regular grid.
for r_idx in range(dim):
	tree_list = grid[r_idx]
	for t_idx in range(dim):
		if not visibilities[r_idx][t_idx]:
			visibilities[r_idx][t_idx] = is_visible(t_idx, tree_list)
		
# Iterate through the rotated grid.
for c_idx in range(dim):
	tree_column = rotated_grid[c_idx]
	for t_idx in range(dim):
		if not visibilities[t_idx][c_idx]:
			visibilities[t_idx][c_idx] = is_visible(t_idx, tree_column)

# Count visible trees.
answer = 0
for row in visibilities:
	for vis in row:
		if vis:
			answer +=1
print(f'Part 1 answer is {answer}.')



# ---------------------- Part 2

# Calculate scenic score for a single tree. Requires tree's coordinates
# in the grid as arguments.
def calculate_scenic_score(given_r_idx, given_t_idx):
	
	# Each range iterates from the closest adjacent tree until the edge
	# of the grid.
	ranges_ = {
		'up': range(given_r_idx - 1, -1, -1),
		'down': range(given_r_idx + 1, dim),
		'right': range(given_t_idx + 1, dim),
		'left': range(given_t_idx - 1, -1, -1),
	}
	
	# How tall of a tree will block the view?
	enough_to_block = grid[given_r_idx][given_t_idx]
	
	# Will be populated with 4 scenic scores, 1 for each direction.
	scores = []
	
	for dir_, range_ in ranges_.items():
		score = 0
		
		# changing_idx means row index when going up or down and tree
		# index when going right or left
		for changing_idx in range_:
			score += 1
			
			if dir_ in ('up', 'down'):
				if grid[changing_idx][given_t_idx] >= enough_to_block:
					break
					
			if dir_ in ('right', 'left'):
				if grid[given_r_idx][changing_idx] >= enough_to_block:
					break
					
		scores.append(score)
		
	return scores[0] * scores[1] * scores[2] * scores[3]

# Calculate scenic scores for all trees and keep the highest in memory.
answer = 0
for r_idx in range(dim):
	for t_idx in range(dim):
		answer = max([calculate_scenic_score(r_idx, t_idx), answer])
print(f'Part 2 answer is {answer}.')
