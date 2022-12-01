import re

with open('aoc.txt') as file:
    answers = file.read()

answers = re.split(r'\n\n', answers)
for i in range(len(answers)):
    answers[i] = re.split(r'\n', answers[i])

# to get rid of the extra \n at the end of the .txt file
answers[len(answers)-1].remove('')

def total_common_answers(group):
    all_letters = 'qwertyuiopasdfghjklzxcvbnm'
    common_letters = 'qwertyuiopasdfghjklzxcvbnm'

    for person in group:
        for letter in all_letters:
            if not letter in person:
                common_letters = common_letters.replace(letter, '')

    return len(common_letters)

total = 0
for group in answers:
    total += total_common_answers(group)

print(total)
