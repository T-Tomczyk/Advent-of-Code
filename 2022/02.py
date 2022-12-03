with open('02.in', 'r') as f:
	guides = f.readlines()


# Part 1

def get_result(guide):
	shape_scores = {
		'X': 1,
		'Y': 2,
		'Z': 3,
	}

	round_scores = {
		'A X': 3,
		'A Y': 6,
		'A Z': 0,
		'B X': 0,
		'B Y': 3,
		'B Z': 6,
		'C X': 6,
		'C Y': 0,
		'C Z': 3,
	}

	result = 0

	result += shape_scores[guide[2]]
	result += round_scores[guide[:3]]

	return result

total = 0

for guide in guides:
	total += get_result(guide)

print(total)


# Part 2

def get_result(guide):
	round_scores = {
		'X': 0,
		'Y': 3,
		'Z': 6
	}

	shape_scores = {
		'A X': 3,
		'A Y': 1,
		'A Z': 2,
		'B X': 1,
		'B Y': 2,
		'B Z': 3,
		'C X': 2,
		'C Y': 3,
		'C Z': 1,
	}

	result = 0

	result += shape_scores[guide[:3]]
	result += round_scores[guide[2]]

	return result

total = 0

for guide in guides:
	total += get_result(guide)

print(total)
