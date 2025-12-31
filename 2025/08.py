import sys
test = any('t' in arg for arg in sys.argv)
inp = open('08.inp' if not test else '08.test').read()
lines = inp.strip().splitlines()

ans = 0

nails = 8 if test else 256

ns = inp.strip().split(',')
ns = list(map(int, ns))
from collections import defaultdict
# pt = defaultdict(int)
pts = []

import math
on = -1
for n in ns:
    # n -= 1
    # ans += pt[n]
    if on != -1 and (n-on)%nails == nails//2:
        # ans += 1
        pass
    # mn = min(on, n)
    # mx = max(on, n)
    ca = 0
    if on != -1:
        ln = min(n, on)
        gn = max(n, on)
        for s,e in pts:
            cs,ce = ln,gn
            if s == cs or s == ce or e == cs or e == ce:
                continue
            if e < s:
                e += nails
            if ce < cs:
                ce += nails
            if (cs < s and s < ce and ce < e) or (
                s < cs and cs < e and e < ce
            ):
                ca += 1
                # print(s%nails, e%nails, cs%nails, ce%nails)


        pts.append((ln,gn))
    # print(ca)
    ans += ca
    # ans = max(ans, ca)
    on = n
    # x = math.cos(n*math.pi/nails)
    # y = math.sin(n*math.pi/nails)
    # print(y)
print('p2', ans)

ans = 0
for cs in range(1, nails+1):
    for ce in range(cs+1, nails+1):
        ca = 0
        for s,e in pts:
            # if s == cs or s == ce or e == cs or e == ce:
            #     continue
            if e < s:
                e += nails
            if ce < cs:
                ce += nails
            if (cs < s and s < ce and ce < e) or (
                s < cs and cs < e and e < ce
            ):
                ca += 1
        if (cs, ce) in pts: ca += 1
        # print(cs, ce, ca)
        ans = max(ca, ans)
print(pts)
print(len(pts))
print('p3', ans)