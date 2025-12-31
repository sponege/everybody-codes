import sys
import time
from things import *
from collections import deque
test = any('t' in arg for arg in sys.argv)
# real_print=print
# if not test:
#     old_p = print
#     print = lambda *c: 1


inp = open('19.txt' if not test else '19.two').read()
lines = inp.splitlines()

dirs=lines[0]
g = [list(l) for l in lines[2:]]

h=len(g)
w=len(g[0])
og = g
g = []
uid=0
for y in range(h):
    l=[]
    for x in range(w):
        l+=[(x,y)]
    g+=[l]



oo="""ABC
HxD
GFE"""

rr="""HAB
GxC
FED"""

ll="""BCD
AxE
HGF"""

oo=[list(a) for a in oo.splitlines()]
rr=[list(a) for a in rr.splitlines()]
ll=[list(a) for a in ll.splitlines()]

def findPos(c):
    for y in range(h):
        for x in range(w):
            if g[y][x] == c: return (x,y)
    return None

x,y=(0,0)

cd=0
#dirs

origg=[list(l) for l in g]

import math
z=1

count=0
while z > 0:
    d=dirs[cd]
    m={}

    #print(len(loop))

    if d=='R':
        cr=rr
    else:
        cr=ll
    oldz=1
    for _l in range(1):
        for dx in range(3):
            for dy in range(3):
                cx,cy=x+dx,y+dy
                m[oo[dy][dx]]=g[cy][cx]
        for dx in range(3):
            for dy in range(3):
                cx,cy=x+dx,y+dy
                g[cy][cx]=m[cr[dy][dx]]

    x+=1
    cd+=1
    cd%=len(dirs)
    if x+2>=w:
        x=0
        y+=1
        if y+2>=h:
            y=0
            cd=0
            if 0:
                print('\n'.join(''.join(l) for l in g))
                time.sleep(.5)
    z-=1
    count+=1
    if count==1:mgone=[list(l) for l in g]

g=origg
mg=mgone
print(g[2][0], mg[2][0])
rz=100
z=math.floor(math.log(rz)/math.log(2))
z=1
if z != 1:
    rz-=2**(z-1)
    print(rz,z,'sigma')
    z*=(w-2)*(h-2)
    g=origg
    #z=1048576000
z-=1
mg=mgone

while z > 0:
    bng=[]
    for y in range(h):
        l=[]
        for x in range(w):
            cx,cy=mg[y][x]
            l+=[origg[cy][cx]]
        bng+=[l]
    mg=bng    
    z-=1

z=0

while z > 0:
    bng=[]
    for y in range(h):
        l=[]
        for x in range(w):
            cx,cy=mg[y][x]
            l+=[g[cy][cx]]
        bng+=[l]
    g=bng    
    z-=1

z=rz
mg=mgone
print('z is', z, mg[2][0], g[2][0])
if z > 0:
    while z > 0:
        bng=[]
        for y in range(h):
            l=[]
            for x in range(w):
                cx,cy=mg[y][x]
                l+=[g[cy][cx]]
            bng+=[l]
        g=bng    
        z-=1

ng=[]
for y in range(h):
    l=[]
    for x in range(w):
        cx,cy=g[y][x]
        l+=og[cy][cx]
    ng+=[l]
g=ng
print('\n'.join(''.join(l) for l in g))
print(x,y)
