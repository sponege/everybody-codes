import sys
test = any('t' in arg for arg in sys.argv)
inp = open('16.inp' if not test else '16.test').read()

l = list(map(int, inp.split(',')))

ans = []

while 1:
    br = 1
    
    for i, n in enumerate(l):
        if l[i] > 0:
            ans += [i+1]
            # print(l)
            break
    for i, n in enumerate(l):
        if l[i] > 0 and (i+1)%ans[-1] == 0:
            br = 0
            l[i] -= 1
    if br: break

print(','.join(map(str, ans)))