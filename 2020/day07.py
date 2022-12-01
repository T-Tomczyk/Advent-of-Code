# Part 1

# with open('day07.txt') as file:
#     rules_list = file.readlines()
#
# for i in range(len(rules_list)):
#     rules_list[i] = rules_list[i].replace('contain', '')
#     rules_list[i] = rules_list[i].replace('no', '')
#     rules_list[i] = rules_list[i].replace('other', '')
#     rules_list[i] = rules_list[i].replace('bag,', '')
#     rules_list[i] = rules_list[i].replace('bags,', '')
#     rules_list[i] = rules_list[i].replace('bag.', '')
#     rules_list[i] = rules_list[i].replace('bags.', '')
#     rules_list[i] = rules_list[i].replace('bags', '')
#     rules_list[i] = rules_list[i].split()
#
# rules = {}
# for rule in rules_list:
#     outer_bag = rule[0]+rule[1]
#     rules[outer_bag] = []
#     for i in range(3, len(rule), 3):
#         rules[outer_bag].append(rule[i]+rule[i+1])
#
# def change_container_to_contents(container_to_change):
#     result = []
#     for color in rules[container_to_change]:
#         result.append(color)
#         for c in change_container_to_contents(color):
#             result.append(c)
#
#     return list(set(result))
#
# results = {}
# for color in rules.keys():
#     results[color] = change_container_to_contents(color)
#
# counter = 0
# for value in results.values():
#     for color in value:
#         if color == 'shinygold':
#             counter += 1
#
# print(counter)


# Part 2
with open('day07.txt') as file:
    rules_list = file.readlines()

for i in range(len(rules_list)):
    rules_list[i] = rules_list[i].replace('contain', '')
    rules_list[i] = rules_list[i].replace('no', '')
    rules_list[i] = rules_list[i].replace('other', '')
    rules_list[i] = rules_list[i].replace('bag,', '')
    rules_list[i] = rules_list[i].replace('bags,', '')
    rules_list[i] = rules_list[i].replace('bag.', '')
    rules_list[i] = rules_list[i].replace('bags.', '')
    rules_list[i] = rules_list[i].replace('bags', '')
    rules_list[i] = rules_list[i].split()

rules = {}
for rule in rules_list:
    outer_bag = rule[0] + rule[1]
    rules[outer_bag] = []
    for i in range(2, len(rule), 3):
        for j in range(int(rule[i])):
            rules[outer_bag].append(rule[i+1]+rule[i+2])

# # debug print
# for k, v in rules.items():
#     print(k.rjust(15) + ':', v)
# print('')
# # debug print

def bag_substitution(bag_to_sub):
    result = []

    for c1 in rules[bag_to_sub]:
        result.append(c1)
        for c2 in bag_substitution(c1):
            result.append(c2)

    return result

print(len(bag_substitution('shinygold')))
