import sys
test = any('t' in arg for arg in sys.argv)

inp = open('01.inp' if not test else '01.test').read()
lines = inp.splitlines()

a=lines[0].split(',')
b=lines[2]

i=0

for c in b.split(','):
    # print(c)
    # oi = i
    i=0
    n=c[1:]
    n=int(n)
    d=c[0]
    i += n * (-1 if d == 'L' else 1)
    # i = max(0, i)
    # i = min(i, len(a)-1)
    i %= len(a)
    print(i, a[i])
    # print(a[i])
    a[0], a[i] = a[i], a[0]
    print(a)
print(a[0])
