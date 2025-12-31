import sys
from things import *
from collections import deque, defaultdict
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


ps=deque()

uid=1
uids={}
for x in range(w):
    for y in range(h):
        if g[y][x]=='P': ps.append([x,y,set(),uid,[]]); uids[uid]=(x,y); uid+=1

print(ps)
seen=set()
ans=0

trees=inp.count('P')

dp=defaultdict(dict)

run=1
ans=0
while run:
    nps=deque()
    print(len(ps), ans)
    while len(ps):
        #print(len(ps))
        x,y,seen,uid,pth=ps.popleft()
        #print(x,y)

        for dx,dy in [[0,1],[0,-1],[-1,0],[1,0]]:
            nx,ny=(x+dx,y+dy)
            if (nx,ny) in seen: continue
            if not check(nx,ny): continue
            if g[ny][nx] == '.':
                if (nx,ny) not in dp or uid not in dp[(nx,ny)] or ans < dp[(nx,ny)][uid][0]: dp[(nx,ny)][uid] = [ans,pth]
                if len(dp[(nx,ny)].values())==trees:
                    print('ans',sum([a[0] for a in dp[(nx,ny)].values()])+1,(nx,ny))
                    print(dp)
                    print(uids)
                    run=0
                    exit()
            nps.append([nx,ny,seen|set({nx,ny}),uid,pth+[(nx,ny)]])#+[(nx,ny)]])
    ps=nps
    ans+=1
print(run)
