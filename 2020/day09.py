from day09input import *
# full = (
# 35,
# 20,
# 15,
# 25,
# 47,
# 40,
# 62,
# 55,
# 65,
# 95,
# 102,
# 117,
# 150,
# 182,
# 127,
# 219,
# 299,
# 277,
# 309,
# 576,
# )

preamble_len = 25

def is_valid(index):
    number = full[index]

    i = index - 1
    while i >= index - preamble_len - 1:
        j = i - 1
        while j >= index - preamble_len:
            if full[i] + full[j] == number:
                return True
            j -=  1
        i -= 1

    return False

for index in range(preamble_len, len(full)):
    if is_valid(index) == False:
        invalid_num = full[index]
        invalid_num_idx = index
        break

lowerband_idx = 0
set_len = 2
while True:
    set_sum = sum(full[lowerband_idx: lowerband_idx+set_len])
    if set_sum < invalid_num:
        set_len += 1
    elif set_sum > invalid_num:
        set_len = 2
        lowerband_idx += 1
    else:
        result = []
        for result_idx in range(lowerband_idx, lowerband_idx + set_len):
            result.append(full[result_idx])
        result = sorted(result)
        print(f'smallest + largest = {result[0] + result[len(result)-1]}')
        break




# Part 1
# from day09input import *
#
# preamble_len = 25
#
# def is_valid(index):
#     number = full[index]
#
#     i = index - 1
#     while i >= index - preamble_len - 1:
#         j = i - 1
#         while j >= index - preamble_len:
#             if full[i] + full[j] == number:
#                 return True
#             j -=  1
#         i -= 1
#
#     return False
#
# invalid_found = False
# for index in range(preamble_len, len(full)):
#     if is_valid(index) == False:
#         print(f'invalid number found: {full[index]} at index {index}')
#         invalid_found = True
#         break
#
# if invalid_found == False:
#     print('all numbers are valid')
