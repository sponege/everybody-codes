import sys
import time
from things import *
from collections import deque
test = any('t' in arg for arg in sys.argv)
# real_print=print
# if not test:
#     old_p = print
#     print = lambda *c: 1

inp = open('20.txt' if not test else '20.test').read()
lines = inp.splitlines()

g = [list(l) for l in lines]

h=len(g)
w=len(g[0])

a=1000

#0123
#>v<>^

ds=[[1,0],[0,1],[-1,0],[0,-1]]

sy=0
print(g[0])
sx=g[sy].index('S')
tl=101
from collections import deque
ps=deque([[sx,sy,1000,3,[]]])

ans=1000

dp={}
cost={'+': 1, '-': -2, '.': -1, 'S': -1}
thing=None
while tl>0:
    nps=deque()
    #print(len(ps),len(dp.keys()))
    while ps:
        cx,cy,s,ld,pth=ps.popleft()
        olds=s
        if s > ans: thing = pth
        ans=max(ans,s)
        for i in range(4):
            s=olds
            if i == ld: continue
            dx,dy=ds[i]
            nx,ny=(cx+dx,cy+dy)
            if not (0 <= nx < w and 0 <= ny < h and g[ny][nx] not in '#'): continue
            s+=cost[g[ny][nx]]
            k=(nx,ny)
            if k not in dp or s>dp[k]:
                dp[k]=s
            else: continue
            nps.append([nx,ny,s,(i+2)%4,pth+[(nx, ny, g[ny][nx])]])
    ps=nps
    tl-=1
print(ans)
