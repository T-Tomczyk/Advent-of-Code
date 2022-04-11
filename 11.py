with open('11.in','r') as f:
    inp = [int(x) for x in list(f.read().replace('\n', ''))]

def print_inp(inp):
    for i in range(0,100,10):
        print(inp[i:i+10])
    print()

def increase_all_by_1(inp):
    for idx in range(len(inp)):
        inp[idx] += 1

def increase_adjacent_by_1(inp, idx):
    in_top_row = idx < 10
    in_bot_row = idx > 89
    in_left_col = idx % 10 == 0
    in_right_col = (idx - 9) % 10 == 0

    if not in_top_row and not in_left_col:
        inp[idx - 11] += 1
    if not in_top_row:
        inp[idx - 10] += 1
    if not in_top_row and not in_right_col:
        inp[idx - 9] += 1
    if not in_left_col:
        inp[idx - 1] += 1
    if not in_right_col:
        inp[idx + 1] += 1
    if not in_bot_row and not in_left_col:
        inp[idx + 9] += 1
    if not in_bot_row:
        inp[idx + 10] += 1
    if not in_bot_row and not in_right_col:
        inp[idx + 11] += 1

def part1(inp, steps):
    flashes = 0

    for step in range(1, steps + 1):
        increase_all_by_1(inp)
        flashed_this_step = set()

        idx = 0
        while idx < 100:
            if inp[idx] > 9 and idx not in flashed_this_step:
                increase_adjacent_by_1(inp, idx)
                flashed_this_step.add(idx)
                flashes += 1
                idx = 0
            else:
                idx += 1

        for idx in flashed_this_step:
            inp[idx] = 0

    return flashes


def part2(inp):
    step = 1
    while True:
        print_inp(inp)
        
        increase_all_by_1(inp)
        flashed_this_step = set()

        idx = 0
        while idx < 100:
            if inp[idx] > 9 and idx not in flashed_this_step:
                increase_adjacent_by_1(inp, idx)
                flashed_this_step.add(idx)
                idx = 0
            else:
                idx += 1

        for idx in flashed_this_step:
            inp[idx] = 0

        if len(flashed_this_step) == 100:
            return step

        step += 1

print(part2(inp))
