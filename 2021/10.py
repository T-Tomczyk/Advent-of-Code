with open('10.in', 'r') as f:
    inp = f.readlines()

def part1(inp):
    score = 0
    scoring = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    for line in inp:
        line = list(line)
        currently_open = []
        chunks = {
            '(': ')',
            '[': ']',
            '{': '}',
            '<': '>',
        }

        for char in line:
            if char in chunks.keys():
                currently_open.append(char)
            if char in chunks.values():
                last_open = currently_open[-1:][0]
                if char == chunks[last_open]:
                    del currently_open[-1]
                else:
                    score += scoring[char]
                    break

    return score

def part2(inp):
    scores = []

    scoring = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4
    }

    chunks = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }

    for line in inp:
        ok = True
        score = 0
        line = list(line.replace('\n',''))
        currently_open = []

        for char in line:
            if char in chunks.keys():
                currently_open.append(char)
            if char in chunks.values():
                last_open = currently_open[-1:][0]
                if char == chunks[last_open]:
                    del currently_open[-1]
                else:
                    ok = False
                    break

        currently_open.reverse()
        if ok:
            for chunk in currently_open:
                score *= 5
                score += scoring[chunk]

        scores.append(score)

    scores = [s for s in scores if not s == 0]
    scores.sort()
    return scores[len(scores)//2]

print(part2(inp))
