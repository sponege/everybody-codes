import sys
from things import *
from collections import deque
test = any('t' in arg for arg in sys.argv)
# real_print=print
# if not test:
#     old_p = print
#     print = lambda *c: 1


inp = open('18.txt' if not test else '18.test').read()
lines = inp.splitlines()
g = [list(l) for l in lines]
h=len(g)
w=len(g[0])

def check(x,y):
    if not ((0 <= x < w) and (0 <= y < h)): return False
    if g[y][x] in '.P': return True
    if g[y][x] in 'P': trees_seen.add((x,y))

    return False

sx,sy=(0,1)

seen=set()
ps=[[0,1]]
ans=0

trees=inp.count('P')
trees_seen=set()

while len(trees_seen)<trees:
    nps=[]
    while len(ps):
        x,y=ps.pop()
        seen.add((x,y))

        for dx,dy in [[0,1],[0,-1],[-1,0],[1,0]]:
            nx,ny=(x+dx,y+dy)
            if not check(nx,ny): continue
            ps.append([nx,ny])#+[(nx,ny)]])
    ans+=1
print(ans)
