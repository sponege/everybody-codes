import sys
from things import *
from collections import deque
test = any('t' in arg for arg in sys.argv)
# real_print=print
# if not test:
#     old_p = print
#     print = lambda *c: 1


inp = open('16.inp1' if not test else '16.test').read()
lines = inp.splitlines()
g = [list(l) for l in lines]

turns = lines[0].split(',')
turns = list(map(int, turns))

a=lines[2:]
def read_symbols(l):
    sym=[]
    while l:
        s=l[:3]
        l=l[4:]
        sym+=[s]
    return sym

a=lines[2:]
a=list(map(read_symbols,a))
print(a)
an=[]
for i in range(len(a)):
    l=[]
    t=0
    while len(a) > t and len(a[t]) > i: l += [a[t][i]]; t+=1
    an+=[l]
a=list(filter(lambda z:z, an))
a=[list(filter(lambda z:z!='   ' and z, l)) for l in a]
print(a)
slot_count=len(a)


strips=[0 for _ in range(slot_count)]
l=100
# l=10
# l=1

for j in range(l):
    print(j, *[a[i][strips[i]] for i in range(slot_count)])

    for i in range(slot_count):
        strips[i]+=turns[i]
        strips[i]%=len(a[i])
print(*[a[i][strips[i]] for i in range(slot_count)])
