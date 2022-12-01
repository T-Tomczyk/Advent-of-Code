# Part 2


# Input manipulation.
import re

with open('day16input2.txt') as f:
    data = re.split(r'\n\n', f.read())

rules = re.split(r'\n', data[0])

fieldnames = [r[:r.index(':')] for r in rules]

for i in range(len(rules)):
    rules[i] = rules[i][rules[i].index(':')+2:]
    rules[i] = [int(x) for x in re.split(r'-', rules[i].replace(' or ', '-'))]

nearby = data[2]
nearby = [x for x in re.split(r'\n', nearby)[1:-1]]
tickets = []
for ticket in nearby:
    tickets.append([int(x) for x in ticket.split(',')])


# Discard invalid tickets.
tickets_to_discard = []

for ticket_idx in range(len(tickets)):
    ticket = tickets[ticket_idx]

    for number in ticket:
        number_passed = False

        for rule in rules:
            if (number >= rule[0] and
            number <= rule[1] or
            number >= rule[2] and
            number <= rule[3]):
                number_passed = True
                break

        if not number_passed:
            tickets_to_discard.append(ticket_idx)
            break

for ticket_id in reversed(tickets_to_discard):
    del(tickets[ticket_id])

print('\nfieldnames:')
print(fieldnames)



# print('\ntickets:')
# print(tickets)

# failed_rules = {number_idx: [rule_idx, rule_idx, rule_idx]}
#           {this num: [failed_rules this rule, and this, and this]}
failed_rules = {}

for number_idx in range(len(tickets[0])):
    if not number_idx in failed_rules:
        failed_rules[number_idx] = []

    for ticket in tickets:
        number = ticket[number_idx]

        for rule_idx in range(len(rules)):
            rule = rules[rule_idx]

            if not (number >= rule[0] and
            number <= rule[1] or
            number >= rule[2] and
            number <= rule[3]):

                if not rule_idx in failed_rules[number_idx]:
                    failed_rules[number_idx].append(rule_idx)

print('\nfailed_rules:')
print(failed_rules)

# followed_rules = {number_idx: [rule_idx, rule_idx, rule_idx]}
#             {this num: [followed_rules this rule, and this, and this]}
followed_rules = {}
all_rules_i = list(range(len(rules)))
for num_idx, failed_rule in failed_rules.items():
    followed_rules[num_idx] = [r for r in all_rules_i if r not in failed_rule]

print('\npotentially followed rules:')
print(followed_rules)

print('\n\nall numbers at index 18:')
templist = []
for ticket in tickets:
    templist.append(ticket[18])
print(templist)

print('\nrules:')
print(rules)

print('\nrule 14:')
print(rules[14])



# finished = False
# while not finished:
#
#     # Look for indexes which follow only one rule.
#     for number, rules in followed_rules.items():
#         if len(rules) == 1:
#             remove_elsewhere = rules[0]
#             except_for = number
#
#     # Remove the found rule from all other number indexes.
#     for number, rules in followed_rules.items():
#         if not number == except_for:
#             if remove_elsewhere in rules:
#                 rules.remove(remove_elsewhere)
#
#     # Check if there is only 1 rule assigned to each number index.
#     # If so, exit the loop.
#     finished = True
#     for rules in followed_rules.values():
#         if len(rules) > 1:
#             finished = False

# print('\nfollowed_rules:')
# print(followed_rules)






















# # Part 1
# import re
#
# with open('day16input2.txt') as f:
#     data = re.split(r'\n\n', f.read())
#
# rules = re.split(r'\n', data[0])
# nearby = data[2].replace('\n', ',')
#
# for i in range(len(rules)):
#     rules[i] = rules[i][rules[i].index(':')+2:]
#     rules[i] = [int(x) for x in re.split(r'-', rules[i].replace(' or ', '-'))]
#
# nearby = [int(x) for x in re.split(r',', nearby)[1:-1]]
#
# total = 0
# for number in nearby:
#
#     times_invalid = 0
#
#     for rule in rules:
#         if (number < rule[0] or
#             number > rule[3] or
#             (number > rule[1] and number < rule[2])
#            ):
#            times_invalid += 1
#
#     if times_invalid == len(rules):
#            total += number
#
# print(f'total: {total}')
