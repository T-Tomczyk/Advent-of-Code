with open('day19input1.txt') as f:
    data = f.read().split('\n\n')

msgs = data[1].split('\n')[:-1]

rules_list = data[0].split('\n')
rules = {}
for rule in rules_list:
    colon = rule.index(':')
    rule_index = int(rule[:colon])

    # case when "a" or "b"
    if '"' in rule:
        rule_content = rule[-2]

    # case with alternative rules
    elif '|' in rule:
        pipe = rule.index('|')
        rule_content = [
            rule[colon+2:pipe-1].split(' '),
            rule[pipe+2:].split(' ')
        ]

    # case when no alternatives
    else:
        rule_content = rule[colon+2:].split(' ')

    rules[str(rule_index)] = rule_content

for k,v in rules.items():
    print(k, v)

converted_rules = []
for number in rules['0']:
    converted_rules.append(rules[number])
print('\n\n', converted_rules)
