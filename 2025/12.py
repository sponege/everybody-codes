import sys
test = any('t' in arg for arg in sys.argv)
inp = open('12.inp' if not test else '12.test').read()
lines = inp.strip().splitlines()
# print(lines)
g = [list(map(int, list(l))) for l in lines]
# print(g)
# exit()
perms=[]
for _ in range(3):
    starts = []

    for sx in range(len(g[0])):
        for sy in range(len(g)):
            starts.append([sx,sy])

    mx = 0
    px,py = -1,-1

    for sx,sy in starts:
        ps=perms+[[sx,sy]]

        def get(x,y):
            if x < 0 or y < 0 or x >= len(g[0]) or y >= len(g):
                return float('inf')
            return g[y][x]

        seen=set()
        while ps:
            x,y = ps.pop()
            if (x,y) in seen: continue
            seen.add((x,y))
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                cx, cy = x+dx, y+dy
                # print(x, y, cx, cy, get(x,y), get(cx,cy))
                if get(x,y) >= get(x+dx,y+dy):
                    ps.append([x+dx,y+dy])
        ans = len(seen)
        # print(ans)
        if ans > mx:
            mx = ans
            px = sx
            py = sy
        
    perms.append([px,py])
    print(mx)