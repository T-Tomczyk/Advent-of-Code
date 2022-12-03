with open('03.in', 'r') as f:
    rucksacks = [l.replace('\n', '') for l in f.readlines()]

def get_item_priority(item):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    combined = list(lower + upper)
    return combined.index(item) + 1

def part1():
    sum = 0
    for rucksack in rucksacks:
        halfpoint = len(rucksack) // 2 

        comp1 = rucksack[:halfpoint]
        comp2 = rucksack[halfpoint:]

        comp1_unique = set(list(comp1))

        for item in list(comp2):
            if item in comp1_unique:
                sum += get_item_priority(item)
                break

    return sum

def part2():

    sum = 0

    for idx in range(0, len(rucksacks)-2, 3):

        sacks = [
            set(rucksacks[idx]),
            set(rucksacks[idx+1]),
            set(rucksacks[idx+2]),
        ]

        seen = {}

        for sack in sacks:
            for item in sack:
                if item in seen:
                    seen[item] += 1
                    if seen[item] == 3:
                        sum += get_item_priority(item)
                        break
                else:
                    seen[item] = 1

    return sum

print(part2())

    