with open('day11input1.txt') as f:
    data = [line.replace('\n', '') for line in f.readlines()]

# Add frame around the seating area.
horizontal = 'O'*len(data[0])
data = [horizontal] + data + [horizontal]

for i in range(len(data)):
    data[i] = 'O' + data[i] + 'O'
    data[i] = list(data[i])


def go_up(r, c):
    while True:
        if data[r-1][c] == 'O' or data[r-1][c] == 'L':
            return False
        elif data[r-1][c] == '#':
            return True
        else:
            r -= 1

def go_down(r, c):
    while True:
        if data[r+1][c] == 'O' or data[r+1][c] == 'L':
            return False
        elif data[r+1][c] == '#':
            return True
        else:
            r += 1

def go_right(r, c):
    while True:
        if data[r][c+1] == 'O' or data[r][c+1] == 'L':
            return False
        elif data[r][c+1] == '#':
            return True
        else:
            c += 1

def go_left(r, c):
    while True:
        if data[r][c-1] == 'O' or data[r][c-1] == 'L':
            return False
        elif data[r][c-1] == '#':
            return True
        else:
            c -= 1

def go_up_right(r, c):
    while True:
        if data[r-1][c+1] == 'O' or data[r-1][c+1] == 'L':
            return False
        elif data[r-1][c+1] == '#':
            return True
        else:
            r -= 1
            c += 1

def go_up_left(r, c):
    while True:
        if data[r-1][c-1] == 'O' or data[r-1][c-1] == 'L':
            return False
        elif data[r-1][c-1] == '#':
            return True
        else:
            r -= 1
            c -= 1

def go_down_right(r, c):
    while True:
        if data[r+1][c+1] == 'O' or data[r+1][c+1] == 'L':
            return False
        elif data[r+1][c+1] == '#':
            return True
        else:
            r += 1
            c += 1

def go_down_left(r, c):
    while True:
        if data[r+1][c-1] == 'O' or data[r+1][c-1] == 'L':
            return False
        elif data[r+1][c-1] == '#':
            return True
        else:
            r += 1
            c -= 1


def occupied_seats_seen(row, col):
    sum = 0
    if go_up(row, col) == True:
        sum += 1
    if go_down(row, col) == True:
        sum += 1
    if go_right(row, col) == True:
        sum += 1
    if go_left(row, col) == True:
        sum += 1

    if go_up_right(row, col) == True:
        sum += 1
    if go_up_left(row, col) == True:
        sum += 1
    if go_down_right(row, col) == True:
        sum += 1
    if go_down_left(row, col) == True:
        sum += 1

    return sum


seats_2b_changed = [[],[]]

def update_seats_2b_changed():
    global seats_2b_changed

    result = [[],[]]
    for row_i in range(1, len(data)-1):
        for col_i in range(1, len(data[0])-1):
            if (data[row_i][col_i] == 'L' and
                occupied_seats_seen(row_i, col_i) == 0):
                result[0].append([row_i, col_i])

            elif (data[row_i][col_i] == '#' and
                occupied_seats_seen(row_i, col_i) >= 5):
                result[1].append([row_i, col_i])

    seats_2b_changed = result

# Keep performing changes until reached permanent state.
update_seats_2b_changed()
while len(seats_2b_changed[0]) != 0 or len(seats_2b_changed[1]) != 0:
    for coords in seats_2b_changed[0]:
        data[coords[0]][coords[1]] = '#'

    for coords in seats_2b_changed[1]:
        data[coords[0]][coords[1]] = 'L'

    update_seats_2b_changed()

# Calculate total occupied at the end.
counter = 0
for row in data:
    for seat in row:
        if seat == '#':
            counter += 1
print(counter)
