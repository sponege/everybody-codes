import sys
test = any('t' in arg for arg in sys.argv)
inp = open('15.inp' if not test else '15.test').read()

x = 0
y = 0
m = {}

cd = 0

for ins in inp.split(','):
    d = ins[0]
    n = ins[1:]

    n = int(n)

    if d == 'L': cd -= 1
    else: cd += 1

    cd %= 4

    ds = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    dx, dy = ds[cd]

    for i in range(n):
        x += dx
        y += dy
        m[(x,y)] = '#'
gx = x
gy = y
del m[(gx,gy)]

# print(m)

seen = set()
seen.add((0,0))
ps = [(0, 0, 0)]

def check(x, y):
    if (x,y) in m:
        return 0
    else: return 1

def manhattan(x, y):
    return abs(gx - x) + abs(gy - y)

while len(ps):
    x, y, s = ps.pop(0)

    if x == gx and y == gy:
        print(s)
        exit()
    for dx, dy in [[1, 0], [0, -1], [-1, 0], [0, 1]]:
        cx = x + dx
        cy = y + dy
        if check(cx, cy) and (cx,cy) not in seen:
            ps.append((cx, cy, s+1))
            seen.add((cx,cy))
            # print(cx, cy, gx, gy)