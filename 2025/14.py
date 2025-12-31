import sys
test = any('t' in arg for arg in sys.argv)
inp = open('14.inp' if not test else '14.test').read()
lines = inp.strip().splitlines()

pattern = [list(l) for l in lines]
g = [['.' for _ in range(34)] for _ in range(34)]

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
def pattern_match():
    global g
    offset = 13
    cx = offset
    cy = offset
    m = 1
    for dy in range(len(pattern)):
        for dx in range(len(pattern[dy])):
            if get(cx+dx, cy+dy) != (1 if pattern[dy][dx] == '#' else 0):
                m = 0
                return m
    return m

cache = set()
lut = {}

pmc = 0

mans = 0

for round in range(1000000000):
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

    k = '\n'.join(''.join(l) for l in g)

    cans = sum([l.count('#') for l in g])

    if pattern_match():
        ans += cans

    if k in cache and pattern_match():
        pmc += 1
        # if pmc > 2: break
        # print(ans + (((ans - lut[k][1]) * ((1000000000 - round) // (round - lut[k][0])))), (1000000000 - round) // (ans - lut[k][0]), round, ans, lut[k])
        asdf = ans + (((ans - lut[k][1]) * ((1000000000 - round) // (round - lut[k][0]))))
        mans = max(asdf, mans)
        print(mans)

    cache.add(k)
    lut[k] = (round, ans)


