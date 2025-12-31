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

    return False


sps=deque()

for x in range(w):
    for y in range(h):
        if g[y][x]=='.': sps.append([[x,y]])

trees=inp.count('P')
realans=float('inf')
while sps:
    print(len(sps))
    ps=sps.popleft()
    seen=set()
    ans=0
    cur=0
    trees_seen=set()
    while len(trees_seen)<trees:
        nps=[]
        #print(len(ps), len(trees_seen), trees)
        while len(ps):
            #print(len(ps))
            x,y=ps.pop()
            if g[y][x] in 'P': trees_seen.add((x,y)); ans+=cur
            #print(x,y)
            seen.add((x,y))

            for dx,dy in [[0,1],[0,-1],[-1,0],[1,0]]:
                nx,ny=(x+dx,y+dy)
                if (nx,ny) in seen: continue
                if not check(nx,ny): continue
                nps.append([nx,ny])#+[(nx,ny)]])
        ps=nps
        cur+=1
    realans=min(ans,realans)
print(realans)
