import sys
test = any('t' in arg for arg in sys.argv)
rp = 1000
inp = (open('07.inp' if not test else '07.test').read())
lines = inp.strip().splitlines()

ans = 0

names = lines[0].split(',')

rules = inp.split('\n\n')[1].splitlines()

print(names, rules)
ni = 1

real = []

from functools import cache

fake = []

justdoit = set()

@cache
def findcount(c, l, n):
    # if c == 'e':print(n,l)
    if l > 11: return 0
    cur = 0
    
    if l >= 7 and l <= 11:
        justdoit.add(n)
        # fake.append(n)
        cur += 1
    for rule in rules:
        ss, es = rule.split(' > ')
        es = es.split(',')
        if c == ss:
            # if l >= 7 and l <= 11:
            #     fake.append(n)
            #     cur += 1
            cur += sum(findcount(ee, l+1, n+ee) for ee in es)
            # s = 1
            # print(rule, name, name[i:i+2])
            # break
    return cur

for name in names:
    f = 0
    # print(list(enumerate(name)))
    for i, c in enumerate(name):
        if i == len(name) - 1: break
        s = 0
        for rule in rules:
            ss, es = rule.split(' > ')
            es = es.split(',')
            if c == ss and name[i+1] in es:
                s = 1
                # print(rule, name, name[i:i+2])
                break
        # print(c, s)
        if s == 0:
            f = 1
            # print('wrong')
            break
    # print(name, f)
    if not f:
        # print(name)
        # exit()
        # ans += ni
        real.append((name[-1], len(name), name))
    ni += 1

for c, l, n in real:
    print(n)
    ans += findcount(c, l, n)

# print(ans)
print(len(justdoit))
# fake.sort()
# fake.sort(key=len)
# print('\n'.join(fake))