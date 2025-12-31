test = 0

inp = open('03.inp1' if not test else '03.test').read()
lines = inp.splitlines()
g = lines

ly=len(g)
lx=len(g[0])

total=len(g)*len(g[0])

outer = set()

for y in range(ly):
    for x in range(lx):
        if g[y][x]=='.':outer.add((x,y))

def get(x,y):
    if (x,y) in outer: return 1
    if x < 0 or x >= lx or y < 0 or y >= ly: return 1
    return 0

s=0
while len(outer)<total:
    old=s
    to_add=set()
    for y in range(len(g)):
        for x in range(len(g[0])):
            if get(x,y): continue
            s+=1
            _outer=0
            # for dx,dy in [[0,1],[1,0],[0,-1],[-1,0]]:
            for dx in [0,-1,1]:
                for dy in [0,-1,1]:
                    nx=x+dx
                    ny=y+dy
                    if get(nx,ny): _outer=1
            if _outer: to_add.add((x,y))
    outer=outer.union(to_add)
    print(s-old)


print(s)

