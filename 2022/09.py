with open('09.in', 'r') as f:
	instructions = [l.strip() for l in f.readlines()]

# How the x, y coordinates change based on direction.
coord_changes = {
	'U': (0, 1),
	'R': (1, 0),
	'D': (0, -1),
	'L': (-1, 0)
}


# ------------------ Part 1 ------------------ 

# Current position of head.
H = [0,0]

# Current position of tail.
T = [0,0]

# Will store all positions ever visited by tail.
T_visited = set()
T_visited.add((0,0))

# One instruction is for example 'U 5'
for ins in instructions:
	
	direction, steps = ins.split()
	
	for _ in range(int(steps)):
	
		# Simulate head's move.
		H[0] += coord_changes[direction][0]
		H[1] += coord_changes[direction][1]
				
		# Check if head and tail are touching.
		dx = abs(H[0] - T[0]) 
		dy = abs(H[1] - T[1])
		if dx < 2 and dy < 2: # Head and tail are touching.
			continue
					
		# Simulate tail's move.
		T[0] += ( H[0] > T[0])
		T[0] -= ( H[0] < T[0])
		T[1] += ( H[1] > T[1])
		T[1] -= ( H[1] < T[1])
					
		# Add current tail's position to T_visited.
		T_visited.add(tuple(T))

print(f'Part 1 answer is {len(T_visited)}')
		
		
# ------------------ Part 2 ------------------ 
		
# Current positions of all knots. Head at index 0, tail at index 9.
pos = [[0,0] for _ in range(10)]

# Will store all positions ever visited by tail.
T_visited2 = set()
T_visited2.add((0,0))

for ins in instructions:
	
	direction, steps = ins.strip().split()
	
	for _ in range(int(steps)):
		
		# Always move the head knot.
		pos[0][0] += coord_changes[direction][0]
		pos[0][1] += coord_changes[direction][1]
		
		# Simulate non-head knots.
		for knot_idx in range(1, 10):
			
			this = pos[knot_idx]
			prev = pos[knot_idx - 1]
			
			# Check if touching.
			dx = abs(prev[0] - this[0])
			dy = abs(prev[1] - this[1])
			if dx < 2 and dy < 2: # Prev and this are touching.
				continue
				
			# Since knots are not touching, move knot.
			this[0] += (prev[0] > this[0])
			this[0] -= (prev[0] < this[0])
			this[1] += (prev[1] > this[1])
			this[1] -= (prev[1] < this[1])
			
			# Add tail's position to T_visited.
			if knot_idx == 9:
				T_visited2.add(tuple(this))
			
print(f'Part 2 answer is {len(T_visited2)}')
