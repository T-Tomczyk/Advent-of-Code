with open('09.in', 'r') as f:
    inp = [list(l) for l in [l.replace('\n', '') for l in f.readlines()]]


### Part 1
def part1(inp):
    risk_levels = []

    for row_idx, row in enumerate(inp):
        for col_idx, digit in enumerate(row):
            adj = []

            if row_idx != 0:
                adj.append(inp[row_idx-1][col_idx])
            if row_idx != len(inp)-1:
                adj.append(inp[row_idx+1][col_idx])
            if col_idx != 0:
                adj.append(inp[row_idx][col_idx-1])
            if col_idx != len(row)-1:
                adj.append(inp[row_idx][col_idx+1])

            low_point = True
            for a in adj:
                if a <= digit:
                    low_point = False

            if low_point:
                risk_levels.append(int(digit) + 1)

    print(sum(risk_levels))


### Part 2
def final_points_finder(row_idx, col_idx, inp):

    all_directions = []

    # Add all adjacent points to the all_directions list.
    # If statements account for the possibility of being on the edge.
    if row_idx != 0:
        all_directions.append([row_idx-1, col_idx])
    if row_idx != len(inp)-1:
        all_directions.append([row_idx+1, col_idx])
    if col_idx != 0:
        all_directions.append([row_idx, col_idx-1])
    if col_idx != len(inp[row_idx])-1:
        all_directions.append([row_idx, col_idx+1])

    # Get the current point's height based on coordinates received as input.
    height = int(inp[row_idx][col_idx])

    # Make a list of all adjacent points where the smoke can flow
    # (direction height is smaller than current height).
    flow_directions = []
    for dir in all_directions:
        if int(inp[dir[0]][dir[1]]) < height:
            flow_directions.append(dir)

    final_points = set()

    # If reached a low point, add its coordinates to the final_points set,
    # which will contain all possible coordinates where smoke could
    # end up flowing to.
    if len(flow_directions) == 0:
        final_points.add((row_idx, col_idx))

    # If not reached a low point, for all found flow_directions, keep looking
    # for smoke flow directions recursively until low points are found.
    else:
        for dir in flow_directions:
            final_points.update(final_points_finder(dir[0], dir[1], inp))

    return final_points


def part2(inp):
    basins = {}

    for row_idx, row in enumerate(inp):
        for col_idx, digit in enumerate(row):
            if int(digit) == 9:
                continue

            final_points = tuple(final_points_finder(row_idx, col_idx, inp))

            if len(final_points) == 1:
                final_points = final_points[0]
                if final_points in basins:
                    basins[final_points].append([row_idx, col_idx])
                else:
                    basins[final_points] = [[row_idx, col_idx]]

    return basins

sizes = []

for v in part2(inp).values():
    sizes.append(len(v))

sizes.sort()

print(sizes[-3] * sizes[-2] * sizes[-1])
