with open('15.in', 'r') as f:
    inp = [[int(n) for n in list(l.strip())] for l in f.readlines()]

for l in inp:
    print(l)

tiles = {
    # coords: lowest score from (0,0)
    # (0,1): s
}
