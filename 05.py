### Very inefficient algorithm :(
### There is no need to make seperate actions depending on the direction of the
### line, at least not to the extent it is done here. Most of it could be done
### with negative and positive values derived from x1, x2, y1 and y2.

with open('05.in', 'r') as f:
	inp = f.readlines()

# convert input
lines = []
for line in inp:
	coords = line.replace('\n', '').split(' -> ')
	lines.append(coords)

# will contain all points in all lines and how many times these points occur
point_occurances = {}

for line in lines:
	# transform strings into lists of integers
	x1, y1 = [int(c) for c in line[0].split(',')]
	x2, y2 = [int(c) for c in line[1].split(',')]

	# create a list with the start and the end of the line
	# this list will be later populated with in-between points
	all_points_curr_line = [line[0], line[1]]

	# if the line is vertical or horizontal
	if x1 == x2 or y1 == y2:

		# depending on the direction of the line, find in-between points
		if x2 != x1 and y1 == y2:
			for x in range(min(x1, x2)+1, max(x1, x2)):
				all_points_curr_line.append(str(x) + ',' + str(y1))
		else:
			for y in range(min(y1, y2)+1, max(y1, y2)):
				all_points_curr_line.append(str(x1) + ',' + str(y))

	# if the line is diagonal
	else:
		a = x1 - x2
		b = y1 - y2

		# line goes from bottom-left to top-right
		if a < 0 and b > 0:
			for inc in range(1, x2-x1):
				all_points_curr_line.append(str(x1+inc) + ',' + str(y1-inc))

		# line goes from top-right to bottom-left
		elif a > 0 and b < 0:
			for inc in range(1, x1-x2):
				all_points_curr_line.append(str(x1-inc) + ',' + str(y1+inc))

		# line goes from bottom-right to top-left
		elif a > 0 and b > 0:
			for inc in range(1, x1-x2):
				all_points_curr_line.append(str(x1-inc) + ',' + str(y1-inc))

		# line goes from top-left to bottom-right
		elif a < 0 and b < 0:
			for inc in range(1, x2-x1):
				all_points_curr_line.append(str(x1+inc) + ',' + str(y1+inc))

	for point in all_points_curr_line:
		if not point in point_occurances:
			point_occurances[point] = 1
		else:
			point_occurances[point] += 1

answer = 0
for v in point_occurances.values():
	if v > 1:
		answer += 1
print(f'The answer is {answer}')
