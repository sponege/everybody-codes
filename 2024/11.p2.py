import sys
test = any('t' in arg for arg in sys.argv)

inp = open('11.inp1' if not test else '11.test').read()
lines = [list(l) for l in inp.splitlines()]

def find(c):
    for y in range(len(lines)):
        if c in lines[y]:
            # print(lines[y])
            return (lines[y].index(c), y)
    return None
def render_grid():
    return '\n'.join(''.join(l) for l in lines)
def check():
    global x,y,a
    a+=1
    if y < 0 or y >= len(lines): return False
    if x < 0 or x >= len(lines[0]): return False
    if lines[y][x] == 'H':
        print('yay')
        lines[y][x]='.'
        return 2
    if lines[y][x] == 'T':
        print('double yay')
        lines[y][x]='.'
        return 1
    else: return False
ans=0
while any('T' in l or 'H' in l for l in lines):
    sp=0
    while 1:
        for c in range(3):
            score=c+1
            c = chr(c+ord('A'))
            x,y=find(c)
            sx,sy=(x,y)
            # print(x,y)
            a=0
            d=0
            x,y=(sx,sy)
            # print(x,y,sp)
            while not (d!=0) and y <= len(lines):
                # print(x,y)
                dir=0
                # x+=1
                # d=check()
                # if d: break
                dir=1
                for _ in range(sp):
                    x+=1
                    y-=1
                    d=check()
                    if d!=0: break
                dir=2
                if d!=0:break
                for _ in range(sp):
                    x+=1
                    d=check()
                    # print(x,y,sp,c)
                    
                    if d!=0:break
                dir=3
                if d!=0:break
                while y <= len(lines):
                    x+=1
                    y+=1
                    # print(x,y,sp,c)

                    d=check()
                    if d!=0:break
                if d!=0:break
            if d!=0:break
            # print(score, sp)
            # print(sp * score, sp, x,y,lines[y],lines[y][x],dir)
        if d!=0: ans += sp * score * d; print(sp, score, d); break
        if not any('T' in l or 'H' in l for l in lines): break
        # print(render_grid())
        sp+=1
print(ans)