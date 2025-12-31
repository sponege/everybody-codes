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
z=100
oldz=z
#z=1048576000
z*=(w-2)*(h-2)
import hashlib
loop=set()
print('z is', z)

while z > 0:
    d=dirs[cd]
    m={}

    has=''.join(''.join(l) for l in g) + f" {x},{y}"
    #has=hashlib.md5(has.encode())
    
    if has in loop and len(loop)>5:
        llen=len(loop)
        tl=z//llen
        print('loop detected!', llen, tl, tl*llen)
        z-=tl*llen
        loop=set()

    loop.add(has)
    #print(len(loop))

    if d=='R':
        cr=rr
    else:
        cr=ll
    oldz=1
    for _l in range(oldz%8):
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
            if 1:
                print('\n'.join(''.join(l) for l in g))
                time.sleep(.5)
    z-=1
print('\n'.join(''.join(l) for l in g))
print(x,y)
