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
# a=[list(filter(lambda z:z, l)) for l in list(zip(*a))]
print(a)
# exit()
slot_count=len(a)


strips=[0 for _ in range(slot_count)]
l=202420242024
byte_coins_won=[]
# l=10
# l=10000
dp={}
# l=1
print(0, *[a[i][strips[i]] for i in range(slot_count)])
# for j in range(l):
j=0
total=0
while j < l:

    for i in range(slot_count):
        strips[i]+=turns[i]
        strips[i]%=len(a[i])
        # print(i, strips[i], a[i])
    result = [a[i][strips[i]] for i in range(slot_count)]
    muzzles = [a[i][strips[i]][1] for i in range(slot_count)]
    muzzles = ''.join(muzzles)
    oldr=result
    result = ''.join(result)
    key = ','.join(map(str, strips))
    if key in dp:
        coins = dp[key]
        leng=len(byte_coins_won)
        loop=(l-j)//leng
        j+=loop*leng
        total+=sum(byte_coins_won)*loop
        dp={}
        byte_coins_won=[]
    # else:
    coins = 0
    p_coins=[]
    for c in set(result):
        if c in muzzles: continue
        if result.count(c)>2: p_coins += [result.count(c)-2]
    if p_coins: coins += sum(p_coins)
    byte_coins_won += [coins]
    dp[key] = coins
    total+=coins
    # print(j+1, *oldr, total)
    j+=1
# print(turns)
print(total)