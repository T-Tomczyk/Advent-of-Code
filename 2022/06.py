with open('06.in', 'r') as f:
	stream = list(f.read())
	
marker_found = False
i = 4
while not marker_found:
	if len(set(stream[i-4:i])) == 4:
		marker_found = True
		print(f'Marker found at {i}.')
	i += 1
	if i > len(stream):
		print('No marker found.')
		break
