'''
start-A
start-b
A-c
A-b
b-d
A-end
b-end

start,A,b,A,c,A,end
start,A,b,A,end
start,A,b,end
start,A,c,A,b,A,end
start,A,c,A,b,end
start,A,c,A,end
start,A,end
start,b,A,c,A,end
start,b,A,end
start,b,end
'''

with open('12.in', 'r') as f:
    INP = [line.strip() for line in f.readlines()]

def find_connections():
    global INP

    connections = {}
    for line in INP:
        left, right = line.strip().split('-')

        if not left in connections:
            connections[left] = set()

        if not right in connections:
            connections[right] = set()

        connections[left].add(right)
        connections[right].add(left)

    return connections

# input: list like ['start', 'A', 'end']
# output: True if valid, False if not
def is_path_valid(path):
    small_nodes = []
    starts_count = 0
    ends_count = 0
    seen_2_small_caves = False

    for node in path:
        if node == 'start':
            starts_count += 1
            if starts_count > 1:
                return False

        elif node == 'end':
            ends_count += 1
            if ends_count > 1:
                return False

        elif node.islower():
            if small_nodes.count(node) == 0:
                small_nodes.append(node)
            elif small_nodes.count(node) == 1 and not seen_2_small_caves:
                small_nodes.append(node)
                seen_2_small_caves = True
            else:
                return False

    return True

ALL_PATHS = []
def find_paths(path):
    global INP
    global ALL_PATHS
    connections = find_connections()

    if path[-1] == 'end':
        ALL_PATHS.append(path)
        return

    for destination in connections[path[-1]]:
        if is_path_valid(path + [destination]):
            find_paths(path + [destination])

find_paths(['start'])
print(len(ALL_PATHS))


'''
build paths:
    go to each connected node except start
after each path built, check if valid
    if so, append to paths
    if not, do not follow the path anymore
after each path built, check if reached the end
    if so, do not follow the path anymore
    if not, continue exploring

So after each addition of a node to a path, three scenarios are possible:
-path valid and not finished
-path valid and finished
-path invalid.

start
    start A [go on]
        start A c [go on]
            start A c A [go on]
                start A c A c [invalid]
                start A c A b [go on]
                    start A c A b d [go on]
                    start A c A b A [go on]
                    start A c A b end [end, add to paths]
                start A c A end [end, add to paths]
        start A b [go on]
        start A end [end, add to paths]
    start b [go on]
'''
