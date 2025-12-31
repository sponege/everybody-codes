import sys
from things import *
from collections import deque
test = any('t' in arg for arg in sys.argv)
# real_print=print
# if not test:
#     old_p = print
#     print = lambda *c: 1

inp = open('15.inp1' if not test else '15.test').read()
lines = inp.splitlines()
g = [list(l) for l in lines]

w = len(g[0])
h = len(g)

sy=0
sx=g[0].index('.')

ps=deque([[sx,sy,0,set(),set(),[]]])
def check(x,y):
    if not ((0 <= x < w) and (0 <= y < h)): return False
    if g[y][x] in '.ABCDEH': return True

    return False
# seen=set()

symbols = (3 if test else 5)
tsymbols = sum(sum(l.count(c) for c in 'ABCDEH') for l in g)
# print(tsymbols)

next_ps=deque()

seen_2=set()

dp={}

while ps:
    # print(len(ps))
    x,y,s,seen,c,pth = ps.popleft()
    # print(g[y][x])
    # print(x,y,len(ps))
    if (x,y) in seen: continue
    seen.add((x,y))
    collected=''.join(sorted(list(c)))
    # if (x,y,s,''.join(sorted(list(c)))) in seen_2: continue
    # print(''.join(sorted(list(c))))
    key=(x,y,collected)
    if key in dp and dp[key] < s: continue
    # seen_2.add((x,y,s,''.join(sorted(list(c)))))
    dp[key]=s
    # print((x,y))
    # print(g[y], g[y][x])

    if g[y][x] in 'ABCDEH' and g[y][x] not in c:
        # print(s)
        c.add(g[y][x])
        next_ps.append([x,y,s,set(),c|set(),pth])

        if g[y][x] == 'C':
            print('if this isnt printed that would suck')
        
        if len(next_ps) == tsymbols:
            print('yahoo!')
            # print(next_ps)
            ps = next_ps
            next_ps = deque()
        # seen=set()
        continue

        # exit()

    if len(c) == symbols and y == 0:
        # print(s,c)
        # print([(t, g[t[1]][t[0]]) for t in pth])
        print(s)
        # seen|=set()
        exit()

    for dx,dy in [[0,1],[0,-1],[-1,0],[1,0]]:
        nx,ny=(x+dx,y+dy)
        if not check(nx,ny): continue
        ps.append([nx,ny,s+1,seen|set(),c|set(),pth])#+[(nx,ny)]])