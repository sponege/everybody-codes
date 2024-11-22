import sys
from things import *
test = any('t' in arg for arg in sys.argv)
real_print=print
if not test:
    old_p = print
    print = lambda *c: 1

inp = open('11.inp1' if not test else '11.test').read()
lines = inp.splitlines()

ms={}
ms[(0, -1)] = 'A'
ms[(0, -2)] = 'B'
ms[(0, -3)] = 'C'

ans = 0
fail = 0

for l in lines:
    # if not test: real_print(l)
    x,y = map(int, l.split())
    y+=1
    ox,oy=(x,y)

    ms[(x,-y)] = '#'

    lowest = None
    def setlowest(n):
        global lowest
        if lowest is None: lowest=n
        else: lowest=min(n,lowest)
    # sp=0
    meteor_steps=0
    tp=(6,6)
    pall=1
    while x > 0 and y > 0:
        # print(x,y)
        for c in range(3):
            # cx,cy = (0, c)
            score=c+1
            ch = chr(c+ord('A'))
            # pred_score = sp * score

            # check initial launch
            for csp in [y-score]:
                # print(sp, y-score, ch, 'cmp')
                # if csp != min(sp, y-score): continue
                # csp = sp
                nx, ny = (csp, score+csp)
                # print((nx,ny),(x,y),csp,ch)
                # if any(x+dp == nx and y+dp == ny for dp in [-1,0]):
                if x == nx and y == ny and meteor_steps == csp:
                    if (nx, -ny) not in ms and ((ox,oy) == tp or pall): ms[(nx,-ny)] = ch
                    # print('t',sp,score)
                    setlowest(csp * score)
                    pass
                # if y-x == score:
                #     if (nx, -ny) not in ms: ms[(nx,-ny)] = ch
                #     setlowest((y-tt) * score)

                # check horizontal
                # csp = y - score
                # csp = sp-1
                # nx, ny = (sp-1, score+csp)
                # and (csp + (x-nx)) == sp 
                if 1757 <= meteor_steps <= 1758: print((nx, ny), nx + csp, (x, y), 'aaa', csp + (x-nx), meteor_steps)
                if nx <= x <= nx + csp and ny == y and meteor_steps == csp + (x-nx)-1:
                    # pass
                    if (x, -y) not in ms and ((ox,oy) == tp or pall): ms[(x,-y)] = ch
                    # print((x,y), (nx,ny))
                    # print('a',csp, score)
                    # print(meteor_steps, csp)
                    setlowest(csp * score)

            # check falling
            
            nx, ny = (x, y)
            # if ny > 1:
            #     nx -= ny - 1
            #     ny = 1
            onx, ony = (nx, ny)


            # for dc in range(ny):
            # sp+1 = ony - dc
            # - dc = sp+1-ony
            # nx, ny = (x, y)
            # dc = -(sp+1-ony)
            dc = 0
            steps = nx
            nx, ny = (onx - dc, ony - dc)
            # if (nx,ny,score,sp) in dp: continue
            # dp.add((nx,ny,score,sp))
            rnx, rny = (nx, ny)
            ny -= score
            # t = abs((2 * nx) - ny)
            t = abs((nx) - (2 * ny))
            # if (x,y) == (5,1):
            #     print(t,'z',c)
            if t % 3 != 0: continue
            t //= 3
            if t == 0: continue
            nx -= t
            ny += t
            #(sp-1)-t+score-dc
            # print(nx,ny,ch,t)


            if ny * 2 == nx and ny > 0:# and ny == sp+1:
                # print(steps, meteor_steps, ch)
                if steps != meteor_steps: continue
                # print((x,y), (nx,ny), t)
                # print(c)
                if (ox,oy) == tp or pall: ms[(rnx,-rny)] = ch
                setlowest(ny * score)
                # print('z', steps, meteor_steps, ny*score)
                pass



            # change = nx - (sp*2)
            # if change < 0: continue
            # ny += change
            # nx -= change
            # if nx % 2 != 0: continue
            # nsp = nx // 2
            # nx -= nsp
            # if ny - c == nx:
            #     print(nsp, score)
            #     setlowest(nsp * score)
            # if onx <= nx <= onx + score and ony == ny:
            #     # pass
            #     print(sp, score)
            #     setlowest(sp * score)
            
            # setlowest(sp * score)
        x-=1
        y-=1
        # print(x,y,'a')
        # sp+=1
        meteor_steps+=1
        if lowest: break
    if lowest: ans += lowest
    print((ox,oy),lowest)
    # if lowest is None:
    #     dc = -(sp+1-oy)
    #     steps = nx
    #     nx, ny = (ox - dc, oy - dc)
    #     # if (nx,ny,score,sp) in dp: continue
    #     # dp.add((nx,ny,score,sp))
    #     rnx, rny = (nx, ny)
    #     ny -= score
    #     # t = abs((2 * nx) - ny)
    #     t = abs((nx) - (2 * ny))
    #     # if (x,y) == (5,1):
    #     #     print(t,'z',c)
    #     if t % 3 != 0: continue
    #     t //= 3
    #     if t == 0: continue
    #     nx -= t
    #     ny += t
    #     #(sp-1)-t+score-dc
    #     # print(nx,ny,ch,t)


    #     if ny * 2 == nx and ny > 0:# and ny == sp+1:
    #         # print(steps, meteor_steps, ch)
    #         if steps != meteor_steps: continue
    #         # print((x,y), (nx,ny), t)
    #         # print(c)
    #         ms[(rnx,-rny)] = ch
    #         setlowest(ny * score)
    #         # print('z', steps, meteor_steps, ny*score)
    #     else: real_print('uh oh')
        
    if lowest is None:
        real_print(lowest,ox,oy)
        print(ox,oy)
        fail = 1
if not test: print = old_p
# if test: print_board(ms)
print(ans)
assert not fail