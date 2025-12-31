import sys
test = any('t' in arg for arg in sys.argv)
inp = open('10.inp' if not test else '10.test').read()
lines = inp.strip().splitlines()

g = [list(l) for l in lines]

def get(x,y):
    if x < 0 or y < 0 or x >= len(g[0]) or y >= len(g):
        return float('inf')
    
    return g[y][x]

kx, ky = 0, 0

for y in range(len(g)):
    if 'D' in g[y]:
        ky = y
        kx = g[y].index('D')
g[ky][kx] = '.'

rms = [
    [2, 1], [2, -1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [1, -2], [-1, -2]
]

rs = [[kx, ky]]

ans = 0

seen = set()

from copy import deepcopy

hideouts = set()
okx, oky = kx, ky
# hideouts.add((kx, ky))

for cy in range(len(g)):
    for cx in range(len(g[cy])):
        if get(cx, cy) == '#':
            hideouts.add((cx,cy))
            g[cy][cx] = '.'

for i in range(3 if test else 20):
    nrs = []
    for kx, ky in deepcopy(rs):
        # print(len(seen))
        for dx, dy in rms:
            cx, cy = kx+dx, ky+dy
            if (cx, cy) not in seen:
                nrs.append((cx, cy))
                seen.add((cx, cy))
    rs = nrs
    seen = set(rs)
    
    for cy in range(len(g)):
        l = ''
        for cx in range(len(g[cy])):
            l += '.' if (cx, cy) not in seen else 'X'
        # print(l)
    
    # for kx, ky in deepcopy(rs):
    #     if get(kx, ky) == 'S':
    #         ans += 1
    #         g[ky][kx] = '.'
    for kx, ky in deepcopy(rs):
        if get(kx, ky) == 'S' and (kx, ky) not in hideouts:
            ans += 1
            g[ky][kx] = 'X'
    # print('\n'.join(''.join(l) for l in g))
    for cy in range(len(g)-1, 0, -1):
        for cx in range(len(g[cy])):
            if get(cx, cy) == 'X':
                g[cy][cx] = '.'


    for cy in range(len(g), 0, -1):
        for cx in range(len(g[0])):
            if cy == len(g):
                if g[cy-1][cx] == 'S': g[cy-1][cx] = '.'
            elif get(cx, cy-1) == 'S' and get(cx, cy) == '.':
                g[cy][cx] = 'S'
                g[cy-1][cx] = '.'
    
    for kx, ky in deepcopy(rs):
        if get(kx, ky) == 'S' and (kx, ky) not in hideouts:
            ans += 1
            g[ky][kx] = 'X'
    # print()
    # print('\n'.join(''.join(l) for l in g))
    print(ans)

    for cy in range(len(g)-1, 0, -1):
        for cx in range(len(g[cy])):
            if get(cx, cy) == 'X':
                g[cy][cx] = '.'
    # if (okx, oky) in hideouts: hideouts.remove((okx, oky))