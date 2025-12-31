import sys
test = any('t' in arg for arg in sys.argv)
inp = open('09.inp' if not test else '09.test').read()
lines = inp.strip().splitlines()

ans = 1
for i,p in enumerate(lines[:2]):
    d = 0
    print(p)
    to = ''
    for j in range(len(p)):
        b = p[j]

        if b != ':' and all(c[j] == b for z,c in enumerate([lines[-1]])):
            to += '!'
            d += 1
        else:
            to += b
    print(to)

    print(d)
    ans *= d
print(ans)