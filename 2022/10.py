with open('10.in') as f:
	program = [l.split() for l in [l.strip() for l in f.readlines()]]

simplified_program = []
for ins in program:
	simplified_program.append(0)
	if len(ins) == 2:
		simplified_program.append(int(ins[1]))
				

# ------------ Part 1 ------------
				
X = 1
total = 0
for cycle, val in enumerate(simplified_program, start=1):
	
	if cycle == 20 or (cycle > 20 and (cycle - 20) % 40 == 0):
		total += X * cycle
		
	X += val
	
print(f'Part 1 answer is {total}\n')
		

# ------------ Part 2 ------------

CRT = [' ']*40*6
		
sprite_pos = []
for i in range(0, len(CRT), 40):
	sprite_pos.append(0 + i)
	sprite_pos.append(1 + i)
	sprite_pos.append(2 + i)

for cycle, val in enumerate(simplified_program, start=1):

	pixel_currently_drawn = cycle - 1
	
	if pixel_currently_drawn in sprite_pos:
		CRT[pixel_currently_drawn] = '#'
		
	sprite_pos = [p + val for p in sprite_pos]
	
for i in range(0, len(CRT), 40):
	print(''.join(CRT[i:i+39]))
