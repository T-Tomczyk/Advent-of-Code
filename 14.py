from datetime import datetime

with open('14.in', 'r') as f:
    template, rules = f.read().split('\n\n')
    template = list(template)
    rules = [r.split(' -> ') for r in rules.split('\n')[:-1]]

# print(template, '\n\n', rules)

def part1(steps):
    global template
    global rules

    for step in range(steps):
        insertions = {}

        for r in rules:
            for t in range(len(template)-1):
                if r[0] == template[t] + template[t+1]:
                    insertions[t+1] = r[1]

        sorted_insertions = {}
        for k in sorted(insertions, reverse=True):
            sorted_insertions[k] = insertions[k]

        for k,v in sorted_insertions.items():
            template = template[:k] + [v] + template[k:]

    counts = []
    unique_letters = set(template)
    for letter in unique_letters:
        counts.append(template.count(letter))

    return max(counts)-min(counts)

# too slow
def part2():
    letter_counts = {}
    for letter in set('QWERTYUIOPASDFGHJKLZXCVBNM'):
        letter_counts[letter] = 0

    def recursion(step, pair):
        global template
        global rules
        nonlocal letter_counts

        triplet = insert_letter(pair)
        pair_one = (triplet[0], triplet[1])
        pair_two = (triplet[1], triplet[2])

        if step == 39:
            letter_counts[triplet[0]] += 1
            letter_counts[triplet[1]] += 1

        else:
            recursion(step+1, pair_one)
            recursion(step+1, pair_two)

    def insert_letter(letters: tuple) -> tuple:
        global rules
        for r in rules:
            if tuple(r[0]) == letters:
                return (letters[0], r[1], letters[1])
        return letters

    for l_idx in range(len(template)-1):
        print(round(l_idx/(len(template)-1)*100), '% done at', datetime.now())
        pair = (template[l_idx], template[l_idx+1])
        recursion(0, pair)

    return letter_countsas
