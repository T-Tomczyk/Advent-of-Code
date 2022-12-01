with open('day11input1.txt') as f:
    inpt = [line.replace('\n', '') for line in f.readlines()]

# Add floor frame around the area.
horizontal = '.'*len(inpt[0])
inpt = [horizontal] + inpt + [horizontal]

for i in range(len(inpt)):
    inpt[i] = '.' + inpt[i] + '.'
    inpt[i] = list(inpt[i])


# For given seat calculate how many adjacent seats are occupied.
def calc_adj_occupied(row, col):
    total = 0

    if inpt[row-1][col-1] == '#':
        total += 1

    if inpt[row-1][col] == '#':
        total += 1

    if inpt[row-1][col+1] == '#':
        total += 1

    if inpt[row][col+1] == '#':
        total += 1

    if inpt[row+1][col+1] == '#':
        total += 1

    if inpt[row+1][col] == '#':
        total += 1

    if inpt[row+1][col-1] == '#':
        total += 1

    if inpt[row][col-1] == '#':
        total += 1

    return total

seats_2b_changed = [[],[]]

def update_seats_2b_changed():
    global seats_2b_changed

    result = [[],[]]
    for row_i in range(1, len(inpt)-1):
        for col_i in range(1, len(inpt[0])-1):
            if (inpt[row_i][col_i] == 'L' and
                calc_adj_occupied(row_i, col_i) == 0):
                result[0].append([row_i, col_i])

            elif (inpt[row_i][col_i] == '#' and
                calc_adj_occupied(row_i, col_i) >= 4):
                result[1].append([row_i, col_i])

    seats_2b_changed = result

# Keep performing changes until reached permanent state.
update_seats_2b_changed()
while len(seats_2b_changed[0]) != 0 or len(seats_2b_changed[1]) != 0:
    for coords in seats_2b_changed[0]:
        inpt[coords[0]][coords[1]] = '#'

    for coords in seats_2b_changed[1]:
        inpt[coords[0]][coords[1]] = 'L'

    update_seats_2b_changed()

# calculate occupied
counter = 0
for row in inpt:
    for seat in row:
        if seat == '#':
            counter += 1
print(counter)
