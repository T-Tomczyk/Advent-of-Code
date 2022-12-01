with open('day13input1.txt') as f:
    _ = f.readline()
    data = f.readline()[:-1].split(',')

increments = list(range(0, len(data)))

for i in range(len(data)-1, -1, -1):
    if data[i] == 'x':
        del(data[i])
        del(increments[i])

for i in range(len(data)):
    data[i] = int(data[i])

print(data)
print(increments, '\n')




# Brute-Force Method
n = data[0]
while True:
    all_good = True
    for i in range(len(data)):
        if (n + increments[i]) % data[i] != 0:
            all_good = False
            break
    if all_good == True:
        break
    else:
        n += data[0]

print(n)


# data = [7, 13]
# increments = [0, 1]
# [77, 168, 259, 350, 441]
#      (168-77)/13 = 7

    # The earliest timestamp that matches the list 17,x,13,19 is 3417.
    # 67,7,59,61 first occurs at timestamp 754018.
    # 67,x,7,59,61 first occurs at timestamp 779210.
    # 67,7,x,59,61 first occurs at timestamp 1261476.
    # 1789,37,47,1889 first occurs at timestamp 1202161486.













# Part 1
# with open('day13input.txt') as f:
#     mytimestamp = f.readline()
#     bus_ids_raw = f.readline()[:-1].split(',')
#
# mytimestamp = int(mytimestamp)
# bus_ids = []
# for id in bus_ids_raw:
#     try:
#         bus_ids.append(int(id))
#     except:
#         pass
#
# print(mytimestamp)
# print(bus_ids)
#
# departures = []
# for id in bus_ids:
#     i = 1
#     while True:
#         if id * i > mytimestamp:
#             departures.append(id*i)
#             break
#         else:
#             i += 1
#
# iwilldepart = min(departures)
# mybusid = bus_ids[departures.index(iwilldepart)]
# ineedtowait = iwilldepart - mytimestamp
# print(mybusid * ineedtowait)
