# 21:10 pizza

import re

with open('day10input2.txt') as file:
    myinput = file.read()

myinput = [int(number) for number in re.split(r'\n', myinput)[:-1]]
myinput = sorted(myinput)

print('')
print(f'sorted myinput = {myinput}')
print('')
# Find all sets of length at least 3, where each consecutive number is
# exactly 1 higher than the one immediately before it.
sets = []
min = 0
max = 2
while max < len(myinput):

    if myinput[max] - myinput[max-1] == myinput[max-1] - myinput[min] == 1:
        while max < len(myinput)-1 and myinput[max+1] - myinput[max] == 1:
            max += 1
        sets.append(myinput[min:max+1])

        min = max + 1
        max = min + 2

    else:
        min += 1
        max += 1

print(sets)

possibilities = {
    3:2,
    4:4,
    5:7
}

# answer should be 19208 (total arangements of adapters)
total_comb = 1
for set in sets:
    total_comb *= possibilities[len(set)]

print('\n' + f'total comb: {total_comb}')
print('')

# 2) W kazdym secie znajdz wszystkie kombinacje bez zwracania od drugiej
# do przedostatniej liczby.


# 3) Wyklucz wszystkie kombinacje, w ktorych sa 3 kolejne liczby
# (lub wiecej niz 3).


# 4) Policz wszystkie pozostale kombinacje w danym secie.


# 5) Oblicz iloczyn wszystkich liczb kombinacji w poszczegolnych setach.





























# Part 1
# myinput = sorted(myinput)
#
# count1 = 1 # outlet to first adapter
# count3 = 1 # last adapter to device
#
# for i in range(1, len(myinput)):
#     diff = myinput[i] - myinput[i-1]
#     if diff == 1:
#         count1 += 1
#     elif diff == 3:
#         count3 += 1
#
# print(count1
