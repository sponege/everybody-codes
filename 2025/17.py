import sys
test = any('t' in arg for arg in sys.argv)
inp = open('17.inp' if not test else '17.test').read()
lines = inp.strip().splitlines()

g = [list(l) for l in lines]

def loc(c):
    for y, l in enumerate(g):
        if c in l: return (l.index(c), y)

vx, vy = loc('@')

ans = 0

from collections import defaultdict
import math
lut = defaultdict(int)

for r in range(100):
    for x in range(len(g[0])):
        for y in range(len(g)):
            if ((x-vx)**2) + ((y-vy)**2) <= r**2 and g[y][x] != '@':
                lut[r] += int(g[y][x]) if g[y][x] != '.' else 0
                g[y][x] = '.'
# print(lut)
    # print('\n'.join(''.join(l) for l in g))
ans = max(lut.values())
for k, v in lut.items():
    if ans == v:
        ans *= k
        break
print(ans)