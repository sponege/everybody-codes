import sys
from things import *
from collections import deque
test = any('t' in arg for arg in sys.argv)
# real_print=print
# if not test:
#     old_p = print
#     print = lambda *c: 1


inp = open('17.txt2' if not test else '17.test').read()
lines = inp.splitlines()
g = [list(l) for l in lines]
h=len(g)
w=len(g[0])


stars = []

for y in range(h):
    for x in range(w):
        if g[y][x] == '*': stars += [(x,y)]

connected=set()

connections=set()

dists=[]

while len(connected) != len(stars):
    for i,(sx,sy) in enumerate(stars):
        print(i,sx,sy)
        #if i in connected: continue
        md = float('inf')
        cs=[]
        for j,(cx,cy) in enumerate(stars):
            if (i == j): continue
            if (i,j) in connections or (j,i) in connections: continue
            # if i in connected: continue
            # if (cx,cy) in connected: continue
            cd = abs(sx-cx) + abs(sy-cy)
            if cd < md:
                md = cd
                cs = [i,j]
        print(md)
        if len(cs)==0:continue
        i=cs[0]
        j=cs[1]
        connected.add(i)
        connected.add(j)
        connections.add((i,j))
        dists += [md]
dists.sort()
assert len(connections) == len(stars)
print(dists)
print(connections)
print(sum(dists[:-1]) + len(stars))
