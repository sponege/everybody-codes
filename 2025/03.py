import sys
test = any('t' in arg for arg in sys.argv)

inp = open('03.inp' if not test else '03.test').read()
lines = inp.splitlines()

a = list(map(int, inp.strip().split(',')))

print(a.count(50))
b = []
ans=0
while len(a):
    d = a
    a = []
    while len(d):
        c = d.pop(0)
        if c not in b:
            b.append(c)
        else:
            a.append(c)
    b=[]
    ans+=1
    # print(len(a), a)
# b.sort(reverse=0)
# print(sum(b[:20]))
# print(ans)

