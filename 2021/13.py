with open('13.in', 'r') as f:
    coords, instructions = f.read().split('\n\n')

# Find dimensions of the paper.
max_x = 0
max_y = 0
for c in coords.split('\n'):
    x = int(c.split(',')[0])
    y = int(c.split(',')[1])
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y
max_x += 1
max_y += 1

# Create a dict of all positions (keys) and whether they are marked (values).
grid = {}
for x in range(max_x):
    for y in range(max_y):
        grid[(x,y)] = '.'

# Mark all the positions in the grid according to input.
for c in coords.split('\n'):
    x = int(c.split(',')[0])
    y = int(c.split(',')[1])
    grid[(x,y)] = '#'

def fold_horizontally(fold_idx):
    global grid
    global max_x
    global max_y

    for y in range(fold_idx + 1, max_y):
        for x in range(max_x):
            if grid[(x,y)] == '#':
                mirrored_idx = y - (2*(y-fold_idx))
                grid[(x,mirrored_idx)] = '#'

    for y in range(fold_idx, max_y):
        for x in range(max_x):
            grid.pop((x,y))

    max_y = fold_idx - 1

def fold_vertically(fold_idx):
    global grid
    global max_x
    global max_y

    for x in range(fold_idx + 1, max_x):
        for y in range(max_y):
            if grid[(x,y)] == '#':
                mirrored_idx = x - (2*(x-fold_idx))
                grid[(mirrored_idx, y)] = '#'

    for x in range(fold_idx, max_x):
        for y in range(max_y):
            grid.pop((x,y))

    max_x = fold_idx - 1

for instruction in instructions.split('\n')[:-1]:
    # Fold direction:
    # y: horizontal, folds up
    # x: vertical, folds left
    direction = instruction[instruction.index('=')-1]

    # At which row or column do we fold?
    fold_idx = int(instruction[instruction.index('=')+1:])

    if direction == 'x':
        fold_vertically(fold_idx)
    else:
        fold_horizontally(fold_idx)

# # Count unmarked positions.
# count = 0
# for v in grid.values():
#     if v == '#':
#         count += 1

for y in range(max_y + 2):
    row = ''
    for x in range(max_x + 1):
        row += grid[(x,y)]
    print(row)
