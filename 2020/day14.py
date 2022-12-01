# Part 2
import itertools
import copy

with open('day14input2.txt') as f:
    data = [line[:-1] for line in f.readlines()]

# input is string, output is integer
def binary36_to_decimal(binary):
    total = 0
    binary = list(binary)
    for i in range(36):
        if binary[i] == '1':
            total += 2 ** (len(binary) - i - 1)
    return total

# input is integer, output is string
def decimal_to_binary36(decimal):
    result = list('0'*36)
    i = 35
    while i >= 0:
        if decimal >= 2**i:
            result[abs(i-35)] = '1'
            decimal -= 2 ** i
        i -= 1
    return ''.join(result)

def apply_mask_to_address(address, mask):
    address = decimal_to_binary36(address)
    result = []
    for i in range(36):
        if mask[i] != '0':
            result.append(mask[i])
        else:
            result.append(address[i])
    return ''.join(result)

# input mask is string, input address is integer, output is list of strings
def calculate_all_addresses(address, mask):
    address = list(apply_mask_to_address(address, mask))

    # this will be populated with all possible addresses and returned
    all_addresses = []

    # at which positions X's are located in the masked address
    X_indexes = []
    for bit_idx in range(len(address)):
        if address[bit_idx] == 'X':
            X_indexes.append(bit_idx)

    # total X's in the masked address
    total_X = address.count('X')

    # all possible sets of 1's and 0's, eg.
    # for total_X = 2 it will be 0,0; 0,1; 1,0; 1,1
    bit_sets = list(itertools.product('01', repeat = total_X))

    for bit_set in bit_sets:
        solved_address = copy.deepcopy(address)
        for i in range(len(X_indexes)):
            solved_address[X_indexes[i]] = bit_set[i]
        all_addresses.append(''.join(solved_address))

    return all_addresses

memory = {}
for line in data:

    if line[:4] == 'mask':
        mask = line[-36:]

    else:
        address = int(line[line.index('[') + 1 : line.index(']')])
        value = int(line[line.index('=') + 2 :])

        all_addresses = calculate_all_addresses(address, mask)

        for adr in all_addresses:
            memory[adr] = value

sum = 0
for number in memory.values():
    sum += number

print(sum)



























# Part 1

# input is string, output is integer
# def binary36_to_decimal(binary):
#     total = 0
#     binary = list(binary)
#     for i in range(36):
#         if binary[i] == '1':
#             total += 2 ** (len(binary) - i - 1)
#     return total
#
# # input is integer, output is string
# def decimal_to_binary36(decimal):
#     result = list('0'*36)
#     i = 35
#     while i >= 0:
#         if decimal >= 2**i:
#             result[abs(i-35)] = '1'
#             decimal -= 2 ** i
#         i -= 1
#     return ''.join(result)
#
# # both inputs are strings, output is string
# def apply_mask_to_binary36(binary, mask):
#     result = []
#     for i in range(36):
#         if mask[i] != 'X':
#             result.append(mask[i])
#         else:
#             result.append(binary[i])
#     return ''.join(result)

# memory = {}
# for line in data:
#     if line[:4] == 'mask':
#         mask = line[-36:]
#     else:
#         address = int(line[line.index('[') + 1 : line.index(']')])
#         decimal = int(line[line.index('=') + 2 :])
#
#         binary = decimal_to_binary36(decimal)
#         masked_binary = apply_mask_to_binary36(binary, mask)
#         new_decimal = binary36_to_decimal(masked_binary)
#
#         memory[address] = new_decimal
#
# sum = 0
# for number in memory.values():
#     sum += number
#
# print(sum)
