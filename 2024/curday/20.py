#!/usr/bin/python3 
import sys
from copy import deepcopy
from collections import defaultdict, deque
import heapq
sys.setrecursionlimit(10**6)
infile = '20.test2' if len(sys.argv)>=2 else '20.txt'
G = open(infile).read().strip()
G = G.split('\n')
R = len(G)
C = len(G[0])

items = set()
for r in range(R):
    for c in range(C):
        if r==0 and G[r][c]=='S':
            sr,sc = r,c
        if G[r][c] not in '#.+-':
            items.add(G[r][c])
print(items)

ds=[[1,0],[0,1],[-1,0],[0,-1]]
cost={'+': 1, '-': -2, '.': -1, 'S': -1}

dp={}

Q = deque([(0,sr,sc, set(), 1000, 3)])
SEEN = set()
hd=0
while Q:
    d,r,c, found, s, dir = Q.popleft()
    olds=s
    if d > hd:
        hd=d
        print(d,len(Q))
#    k=(r,c)
#    v=d+(s*100)
#    if k not in dp or v<dp[k]:
#        dp[k]=v
#    else:
#        continue
    key = (r,c,s,frozenset(found))
    if key in SEEN:
        continue
    SEEN.add(key)
    if r==sr and c==sc and found==items and s>=1000:
        print(d,s)
        break
    #for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
    for i in range(4):
        dr,dc=ds[i]
        s=olds
        rr,cc = r+dr,c+dc
        if 0<=rr<R and 0<=cc<C and G[r][c]!='#':
            if G[r][c] in cost: s+=cost[G[r][c]]
            else: s += -1
#            if s < 1000: continue
            new_found = deepcopy(found)
            if G[rr][cc] in items and ord(G[rr][cc])-ord('A')==len(found) or G[rr][cc]=='S':
                new_found.add(G[rr][cc])
            Q.append((d+1, rr, cc, new_found, s, (i+2)%4))
