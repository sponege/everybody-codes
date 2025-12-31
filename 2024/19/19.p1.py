import sys
from things import *
from collections import deque
test = any('t' in arg for arg in sys.argv)
# real_print=print
# if not test:
#     old_p = print
#     print = lambda *c: 1


inp = open('19.txt' if not test else '19.test').read()
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
z=0
while findPos('>')[1] != findPos('<')[1] or z < 10:
    d=dirs[cd]
    m={}
    if d=='R':
        cr=rr
    else:
        cr=ll
    for dx in range(3):
        for dy in range(3):
            cx,cy=x+dx,y+dy
            m[oo[dy][dx]]=g[cy][cx]
    for dx in range(3):
        for dy in range(3):
            cx,cy=x+dx,y+dy
            g[cy][cx]=m[cr[dy][dx]]


    

    cd+=1
    cd%=len(dirs)

    x+=1
    if x+2>=w:
        x=0
        y+=1
        if y+2>=h:y=0
    print('\n'.join(''.join(l) for l in g))
    print(x,y)
    z+=1
