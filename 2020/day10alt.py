with open('day10input2.txt') as f:
    inp = f.readlines()

inp = [int(number.replace('\n', '')) for number in inp]
inp = sorted(inp)

# Add socket and device.
inp = [0] + inp + [(inp[len(inp)-1]+3)]

# Calculate differences.
diffs = []
for i in range(1, len(inp)):
    diffs.append(inp[i] - inp[i-1])

print(inp)
print(diffs)
print(diffs.count(1) * diffs.count(3))

routes = {}
routes[0] = 1
