import itertools

with open('08.in', 'r') as f:
	inp = f.readlines()


def part1(inp):
    unique_digit_lengths = [2, 3, 4, 7]
    result = 0

    for line in inp:
        all_digits = line[line.index('|') + 1:]
        separate_digits = all_digits.split()
        for digit in separate_digits:
            if len(digit) in unique_digit_lengths:
                result += 1

    print(result)


def find_correct_permutation(clues):
	# takes the first part of a line as input (here called clues)
	# returns the correct permutation of segments (a tuple)

	segments = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
	segments_permutations = list(itertools.permutations(segments, 7))

	'''
	Segment codes used:

	  0
	1   2
	  3
	4   5
	  6
	'''

	correct_digits = {
		(2, 5): 1,
		(0, 2, 3, 4, 6): 2,
		(0, 2, 3, 5, 6): 3,
		(1, 2, 3, 5): 4,
		(0, 1, 3, 5, 6): 5,
		(0, 1, 3, 4, 5, 6): 6,
		(0, 2, 5): 7,
		(0, 1, 2, 3, 4, 5, 6): 8,
		(0, 1, 2, 3, 5, 6): 9,
		(0, 1, 2, 4, 5, 6): 0
	}

	for perm in segments_permutations:
		decoded_digits = []

		for encoded_digit in clues:
			encoded_digit = list(encoded_digit)
			decoded_digit = []
			for letter in encoded_digit:
				decoded_digit.append(perm.index(letter))
			decoded_digit = tuple(sorted(decoded_digit))
			decoded_digits.append(decoded_digit)

		solved = True
		for d in decoded_digits:
			if d not in correct_digits:
				solved = False

		if solved:
			return perm


def decode_single_line(line):
	# takes entire line as input
	# returns the number resulting from decoding the last 4 digits in a line

	clues = line.split('|')[0].strip().split()
	message = line.split('|')[1].strip().split()

	correct_permutation = find_correct_permutation(clues)

	correct_digits = {
		(2, 5): 1,
		(0, 2, 3, 4, 6): 2,
		(0, 2, 3, 5, 6): 3,
		(1, 2, 3, 5): 4,
		(0, 1, 3, 5, 6): 5,
		(0, 1, 3, 4, 5, 6): 6,
		(0, 2, 5): 7,
		(0, 1, 2, 3, 4, 5, 6): 8,
		(0, 1, 2, 3, 5, 6): 9,
		(0, 1, 2, 4, 5, 6): 0
	}

	decoded_digits = []

	for digit in message:
		digit = list(digit)
		decoded_digit = []
		for segment in digit:
			decoded_digit.append(correct_permutation.index(segment))
		decoded_digits.append(correct_digits[tuple(sorted(decoded_digit))])

	answer = ''
	for d in [str(d) for d in decoded_digits]:
		answer += d

	return int(answer)


def part2(inp):
	sum = 0

	for line in inp:
		sum += decode_single_line(line)

	return sum


print(part2(inp))
