# darcula and gotham and twilight

with open('07.in', 'r') as f:
	inp = [int(x) for x in f.read().split(',')]

import statistics

# calculates total fuel usage according to part 1 rules
def total_fuel_usage1(inp, target_pos):
    total = 0
    for pos in inp:
        total += abs(pos - target_pos)
    return total

# calculates total fuel usage according to part 2 rules
cache = {}
def total_fuel_usage2(inp, target_pos):
    if target_pos in cache:
        return cache[target_pos]

    # calculates fuel usage for a single position
    def single_pos_fuel_usage(single_pos, target_pos):
        distance = abs(single_pos - target_pos)

        # it's the formula for 1+2+3...+n for any given n
        return (distance**2 + distance) / 2

    # sum all fuel usages for the entire list
    total = 0
    for pos in inp:
        total += single_pos_fuel_usage(pos, target_pos)

    cache[target_pos] = total
    return total

def solve(inp):
    # make a guess that we have the lowest fuel usage when position = median
    guess = int(statistics.median(inp))

    while True:
        # if next position gives lower fuel usage, increase position
        if total_fuel_usage2(inp, guess+1) <= total_fuel_usage2(inp, guess):
            guess += 1
        # if previous position gives lower fuel usage, decrease position
        elif total_fuel_usage2(inp, guess-1) <= total_fuel_usage2(inp, guess):
            guess -= 1
        # we're at lowest fuel usage possible
        else:
            return f'Guess: {guess}, usage: {total_fuel_usage2(inp, guess)}'

print(solve(inp))
