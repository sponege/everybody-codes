import sys
test = any('t' in arg for arg in sys.argv)

inp = open('01.inp' if not test else '01.test').read()
lines = inp.splitlines()

def mul(x, y):
    return [(x[0] * y[0]) - (x[1] * y[1]), (x[0] * y[1]) + (x[1] * y[0])]



t=[35300,-64910]
# t=[-79067,14068]
A=[-79067,14068]
t=A
sx = t[0]
sy = t[1]
ex = sx + 1000
ey = sy + 1000
m={}
ans=0
r=1

step = 1

for x in range(sx, ex + 1, step):
    for y in range(sy, ey + 1, step):
        m[(x,y)] = '?'

def r(z):
    return [int(z[0]), int(z[1])]
for (x,y) in m.keys():
    a = [0, 0]
    s = 1
    for i in range(100):
        a = mul(a, a)
        a = r(a)
        a[0] /= 100000
        a[1] /= 100000
        a = r(a)
        a[0] += x
        a[1] += y
        a = r(a)
        # if x == 35460 and y == -64910:
        #     print(a,i)
        if not all(-1000000 <= p <= 1000000 for p in a):
            s = 0
            break
    if s:
        m[(x,y)] = '#'
        ans+=1
    else:
        m[(x,y)] = '.'
    # a[0] = round(a[0])
    # a[1] = round(a[1])

for y in range(sy, ey + 1, step):
    l=''
    for x in range(sx, ex + 1, step):
        l += m[(x,y)]
    print(l)
# print(ans)