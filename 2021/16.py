'''
outer layer is always single packet
trailing 0s should be ignored

idx 0,1,2: packet version
idx 3,4,5: type ID

	if type == 4:
		it's literal, encodes a single binary number
		n of 4-bit groups prefixed by 1 bit (total 5)
		last group starts with 0
		to get the number the packet represents, join all the groups of 4 together

	if type != 4:
		it's operator, conatins one or more sub-packets
		idx 6: length type ID

		if length type ID == 0:
			idx from 7 to 22: number representing cumulative length of all sub-packets

		if length type ID == 1:
			idx from 7 to 18: number representing number of sub-packets contained
'''

with open('16.in', 'r') as f:
    inp = f.read().strip()
    full_binary = bin(int(inp, 16))[2:]

version_sum = 0

def packet_analyzer(packet):
	version = int(packet[:3], 2)
	id_type = int(packet[3:6], 2)
	body = tuple(packet[6:])

	version_sum += version

	print(f'{version=}')
	print(f'{id_type=}')
	print(f'{body=}')

	if id_type == 4:
		# is literal

	else:
		# is operator



packet_analyzer(full_binary)
