import sys
from things import *
test = any('t' in arg for arg in sys.argv)
# real_print=print
# if not test:
#     old_p = print
#     print = lambda *c: 1

inp = open('13.inp1' if not test else '13.test').read()
lines = inp.splitlines()
s=set()
ls=set()#leaves
mh=0
for line in lines:
    ins=line.split(',')
    y=-1
    x=0
    z=0
    # s.add((x,y))
    for i in ins:
        c=i[0]
        n=i[1:]
        n=int(n)
        # print(c,n)
        if c == 'U':
            for i in range(n): y += 1; s.add((x,y,z))
        elif c == 'D': 
            for i in range(n): y -= 1; s.add((x,y,z))
        elif c == 'L': 
            for i in range(n): x += 1; s.add((x,y,z))
        elif c == 'R': 
            for i in range(n): x -= 1; s.add((x,y,z))
        elif c == 'F':
            for i in range(n): z += 1; s.add((x,y,z))
        elif c == 'B':
            for i in range(n): z -= 1; s.add((x,y,z))
        mh = max(mh, y)
    ls.add((x,y,z))
    
# s.remove((0,-1))
# print(len([p for p in list(s)]))
# print(len(s))
g={}
rg={}
s=list(s)
ls=list(ls)
for p in s:
    g[(-p[0], -p[1]+1000)]='#'
    rg[p]='#'
for p in ls:
    g[(-p[0], -p[1]+1000)]='!'
    rg[p]='!'
# print_board(g)

move=[]
for x in range(-1,2):
    for y in range(-1,2):
        for z in range(-1,2):
            if [x,y,z].count(0) != 2: continue
            move+=[[x,y,z]]

min_murkiness=None
d=None
from collections import deque
for y in range(mh):
    ms=[]
    # if (0,y,0) not in rg: continue
    murkiness=0
    for gx,gy,gz in ls:
        ps=deque([[0,y,0,0,[]]])
        # seen=set()
        fail=1
        cm=None
        seen=set({(0,y,0)})
        minpath=None
        while len(ps):
            cx,cy,cz,s,pth=ps.popleft()
            # print(len(ps))
            if cx == gx and cy == gy and cz == gz:
                # print('lets go',s)
                if cm is None:cm=s;minpath=pth
                else:cm=min(s,cm);minpath=pth
                fail=0
                break

            for dx,dy,dz in move:
                nx,ny,nz=(cx+dx,cy+dy,cz+dz)
                if (nx,ny,nz) not in rg or (nx,ny,nz) in seen: continue
                ps.append((nx,ny,nz,s+1,pth+[[nx,ny,nz]]))
                seen|=set({(nx,ny,nz)})
        if fail: break
        murkiness+=cm
        ms+=[minpath]
        # print(murkiness)
        # print(seen)
        # print(x,y,z)
        # murkiness+=abs(x)+abs(y-dy)+abs(z)
        # ms+=[[abs(x)+abs(y-dy)+abs(z), abs(x),abs(y-dy),abs(z),x,dy,z]]
    if fail: continue
    # print(murkiness)
    if min_murkiness is None:
        min_murkiness = murkiness
        d=[y,ms]
    else:
        if murkiness < min_murkiness:
            d=[y,ms]
        min_murkiness = min(min_murkiness, murkiness)
print(min_murkiness)