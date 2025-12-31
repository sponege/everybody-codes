import sys
test = any('t' in arg for arg in sys.argv)
inp = open('15.inp' if not test else '15.test').read()

x = 0
y = 0
xlines = []
ylines = []

allx = set()
ally = set()

allx.add(x)
ally.add(y)

cd = 1

l = len(inp.split(','))

i = 0
for ins in inp.split(','):
    i += 1
    # print(ins)
    d = ins[0]
    n = ins[1:]

    n = int(n)

    if d == 'L': cd -= 1
    else: cd += 1

    cd %= 4

    ds = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    dx, dy = ds[cd]
    nx = x + (dx * n)
    ny = y + (dy * n)

    if l == i:
        gx = nx
        gy = ny
        nx -= dx
        ny -= dy

    sx = min(x, nx)
    sy = min(y, ny)
    bx = max(x, nx)
    by = max(y, ny)

    # print(f'\\operatornameline\\left(\\left({x},{y}\\right),\\left({nx},{ny}\\right)\\right)'.replace('line', '{vector}'))

    if sx == bx:
        xlines.append((sx, (sy, by)))
    else:
        ylines.append((sy, (sx, bx)))

    x = nx
    y = ny
    allx.add(x)
    ally.add(y)

# print(ylines)



print('goal', gx, gy)

allx = list(allx)
ally = list(ally)
allx.sort()
ally.sort()

# print('wowzers!')

# print(m)

seen = set()
seen.add((0,0))
ps = [(0, 0, 0, -1)]

# print(xlines)
# print(ylines)

def check(x, y):
    if x == gx and y == gy:
        return 1
    for sx, (sy, by) in xlines:
        if x != sx: continue
        if sy <= y <= by:
            return 0
    for sy, (sx, bx) in ylines:
        if y != sy: continue
        if sx <= x <= bx:
            return 0
    return 1
    

def manhattan(x, y):
    return abs(gx - x) + abs(gy - y)

def checkbounds(x, y):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            cx = dx + x
            cy = dy + y
            if check(cx, cy) == 0:
                return 0
    return 1

noi = 0
while len(ps):
    # print(ps)
    # print(len(ps))
    noi += 1
    x, y, s, odi = ps.pop(0) # x, y, steps, original direction index, tiny steps
    # print(x, y)

    if x == gx and y == gy:
        # print('huh', x, gx, y, gy)
        print('answer', s)
        break
    ds = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    for dx, dy in ds:
        di = ds.index([dx, dy])

        # if odi != -1 and di != odi and checkbounds(dx, dy):
        #     continue
        process = []
        if dx == 1:
            l = [_x for _x in allx if _x >= x]
            if len(l) == 0: continue
            nx = l[0] - 1
            if not check(nx, y): continue
            sa = abs(nx - x)
            cx = nx
            cy = y
            process.append((cx, cy, sa))
            for _ in range(2):
                if check(nx+1, y):
                    nx += 1
                    sa = abs(nx - x)
                    cx = nx
                    cy = y
                    process.append((cx, cy, sa))
        if dy == 1:
            l = [_y for _y in ally if _y >= y]
            if len(l) == 0: continue
            ny = l[0] - 1
            if not check(x, ny): continue
            sa = abs(ny - y)
            cx = x
            cy = ny
            process.append((cx, cy, sa))
            for _ in range(2):
                if check(x, ny+1):
                    ny += 1
                    sa = abs(ny - y)
                    cx = x
                    cy = ny
                    process.append((cx, cy, sa))

        if dx == -1:
            l = [_x for _x in allx if _x <= x]
            if len(l) == 0: continue
            nx = l[-1] + 1
            if not check(nx, y): continue
            sa = abs(nx - x)
            cx = nx
            cy = y
            process.append((cx, cy, sa))
            for _ in range(2):
                if check(nx-1, y):
                    nx -= 1
                    sa = abs(nx - x)
                    cx = nx
                    cy = y
                    process.append((cx, cy, sa))

        if dy == -1:
            l = [_y for _y in ally if _y <= y]
            if len(l) == 0: continue
            ny = l[-1] + 1
            if not check(x, ny): continue
            sa = abs(ny - y)
            cx = x
            cy = ny
            process.append((cx, cy, sa))
            for _ in range(2):
                if check(x, ny-1):
                    ny -= 1
                    sa = abs(ny - y)
                    cx = x
                    cy = ny
                    process.append((cx, cy, sa))
        # cx = x + dx
        # cy = y + dy
        # print('p', process)
        for cx, cy, sa in process:
            if check(cx, cy) and (cx,cy) not in seen:
                ps.append((cx, cy, s + sa, di))
                seen.add((cx,cy))
            # print(cx, cy, gx, gy)
# print(gx, gy)

bounds = 100
for y in range(-bounds, bounds):
    l = ''
    for x in range(-bounds, bounds):
        l += '.' if check(x,y) else '#'
    print(l)