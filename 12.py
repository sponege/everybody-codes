import sys
from things import *
test = any('t' in arg for arg in sys.argv)
real_print=print
if not test:
    old_p = print
    print = lambda *c: 1

inp = open('12.inp1' if not test else '12.test').read()
lines = inp.splitlines()
g = [list(l) for l in lines]
# real_print(len(g[0]), len(g))
# exit()
def find(c):
    for y in range(len(g)):
        if c in g[y]:
            # print(lines[y])
            return (g[y].index(c), y)
    return None

sx,sy=find('E')
ps=[[sx,sy,0,set({(sx,sy)}),0,[]]]
# ps=[[sx,sy,0,0,[]]]

# gx,gy=find('E')

ans=None

dp={}
# seen=set()

def check(x,y):
    if x < 0 or x >= len(g[0]) or y < 0 or y >= len(g) or g[y][x] in '# ': return False
    return True

while len(ps):
    # print(ps[0])
    # real_print(len(ps))
    x,y,steps,seen,old,path=ps.pop()
    # x,y,steps,old,path=ps.pop()
    # seen.add((x,y))
    if steps > 599: continue

    if g[y][x] == 'S':
        # steps += old + 1
        if ans == None: ans = steps
        else: ans = min(steps, ans)
        # real_print(path,steps)
        
        real_print(ans, steps)
        continue

    for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
        nx,ny=(x+dx,y+dy)
        if not check(nx,ny): continue
        if (nx,ny) in seen: continue
        # print(seen,nx,ny)

        # seen.add((nx,ny))
        first=(int(g[y][x]) if g[y][x] not in 'SE' else 0)
        second=(int(g[ny][nx]) if g[ny][nx] not in 'SE' else 0)
        change = min(abs(first-second)+1, (10-abs(first-second))+1)
        steps_cur=steps+change
        if (nx,ny) not in dp or steps_cur <= dp[(nx,ny)]:
            dp[(nx,ny)] = min(steps_cur, dp[(nx,ny)] if (nx,ny) in dp else 9999999999)
            
            print(dp[(nx,ny)], steps_cur)
        else:
        # else:
            
            # print((nx,ny),steps,dp[(nx,ny)],path)
            continue
        # print('yo what the fuck')
        # ps.append([nx,ny,steps,seen|set({(nx,ny)}),(int(g[y][x]) if g[y][x] not in 'SE' else 0),path+[[nx,ny]]])
        # ps.append([nx,ny,steps+change,first,path+[[nx,ny,g[ny][nx],steps+change]]])
        ps.append([nx,ny,steps+change,seen|set({(nx,ny)}),first,[]])#,path+[[nx,ny,g[ny][nx],steps+change]]])
        # ps.append([nx,ny,steps+change,seen|set({(nx,ny)}),first,path+[[nx,ny,g[ny][nx],steps+change]]])
        #,first,second,change,steps,steps+change
        # seen.remove((nx,ny))
real_print(ans)
# print(g)