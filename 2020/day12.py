with open('day12input2.txt') as f:
    data = [ins[:-1] for ins in f.readlines()]

# +N-S, +E-W
ship = [0, 0]
wayp = [10, 1]

for ins in data:

    print('ship now:', ship)
    print('wayp now:', wayp)
    print('next ins:', ins)
    print('')


    if ins[0] == 'N':
        wayp[1] += int(ins[1:])
    elif ins[0] == 'E':
        wayp[0] += int(ins[1:])
    elif ins[0] == 'S':
        wayp[1] -= int(ins[1:])
    elif ins[0] == 'W':
        wayp[0] -= int(ins[1:])

    elif ins == 'R90' or ins == 'L270':
        wayp = [wayp[1], -wayp[0]]
    elif ins == 'L90' or ins == 'R270':
        wayp = [-wayp[1], wayp[0]]
    elif ins[1:] == '180':
        wayp = [-wayp[0], -wayp[1]]

    else:
        ship[0] += int(ins[1:])*wayp[0]
        ship[1] += int(ins[1:])*wayp[1]

print(f'final position of the ship: {ship}')
print(f'final position of the waypoint: {wayp}')
print('manhattan value:', abs(ship[0]) + abs(ship[1]))
