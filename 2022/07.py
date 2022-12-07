with open('07.in', 'r') as f:
	commands = f.readlines()
	
curr_path = '/'
path_sizes = {'/': 0}

for cmd in commands:
	cmd = cmd.split()
	
	# cd
	if cmd[0] == '$' and cmd[1] == 'cd':
		
		# go to root
		if cmd[2] == '/':
			curr_path = '/'	
			
		# go up
		elif cmd[2] == '..':
			if curr_path == '' or curr_path == '/':
				curr_path = '/'
			else:
				# find position of last '/' and remove everything after
				curr_path = curr_path[:curr_path.rfind('/')]
			
		# go to specified
		else:
			if curr_path == '/':
				curr_path = '/' + cmd[2]
			else:
				curr_path = curr_path + '/' + cmd[2]
		
	# found a file in current path
	if cmd[0] != '$' and cmd[0] != 'dir':
		
		# create a list of all paths to increment
		path_elems = curr_path.split('/')
		path_to_increment = ''
		for elem in path_elems:
			path_to_increment += elem + '/'
		
			# increment
			if path_to_increment in path_sizes:
				path_sizes[path_to_increment] += int(cmd[0])
			else:
				path_sizes[path_to_increment] = int(cmd[0])

# Part 1
total = 0
for size in path_sizes.values():
	if size <= 100000:
		total += size
print(total)

# Part 2
total_disk_space = 70000000
needed_disk_space = 30000000
used_space = path_sizes['/']
unused_space = total_disk_space - used_space
min_to_delete = needed_disk_space - unused_space
all_that_meet = []
for size in path_sizes.values():
	if size >= min_to_delete:
		all_that_meet.append(size)
print(min(all_that_meet))
