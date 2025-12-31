import sys
test = any('t' in arg for arg in sys.argv)
inp = open('13.inp' if not test else '13.test').read()
lines = inp.strip().splitlines()

a = [1]
b = []

ff = 1
for l in lines:
    print(l)
    s, e = map(int, l.split('-'))
    if ff:
        a += range(s, e+1)
    else:
        b += range(s, e+1)
    ff = not ff

a += b[::-1]
print(a[202520252025%len(a)])