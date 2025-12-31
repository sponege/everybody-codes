import sys
test = any('t' in arg for arg in sys.argv)
inp = open('14.inp' if not test else '14.test').read()
lines = inp.strip().splitlines()

g = [list(l) for l in lines]

def get(x, y):
    if x < 0 or y < 0 or x >= len(g[0]) or y >= len(g):
        return 0
    return g[y][x] == '#'

def diag(x,y):
    n = 0
    for dx in [-1, 1]:
        for dy in [-1, 1]:
            cx, cy = x+dx, y+dy
            n += get(cx, cy)
    return n
ans = 0
for round in range(2025 ):
    ng = [list(l) for l in g]
    for y in range(len(g)):
        for x in range(len(g[y])):
            if get(x, y):
                if diag(x, y) % 2 == 1:
                    pass
                else:
                    ng[y][x] = '.'
            else:
                if diag(x, y) % 2 == 0:
                    ng[y][x] = '#'
                else:
                    pass
    g = ng

    cans = sum([l.count('#') for l in g])
    ans += cans
print(ans)