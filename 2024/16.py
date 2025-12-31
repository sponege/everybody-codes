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
# print(a)
an=[]
for i in range(len(a)):
    l=[]
    t=0
    while len(a) > t and len(a[t]) > i: l += [a[t][i]]; t+=1
    an+=[l]
a=list(filter(lambda z:z, an))
a=[list(filter(lambda z:z!='   ' and z, l)) for l in a]
# a=[list(filter(lambda z:z, l)) for l in list(zip(*a))]
# print(a)
# exit()
slot_count=len(a)


strips=[0 for _ in range(slot_count)]
l=10
l=256
byte_coins_won=[]
# l=10
# l=10000
# dp={}
# l=1
# print(0, *[a[i][strips[i]] for i in range(slot_count)])
# for j in range(l):
j=0
total=0


ps=[]

def add_strips(l, n):
    return [(i+n)%len(a[j]) for j,i in enumerate(l)]

ps=[[add_strips(strips, n), 0] for n in range(-1,2)]
# print(ps)

ans_max = 0
ans_min = float('inf')

dpg={}
dpl={}

while j < l:
    nps=[]
    # print(j, len(ps))

    while ps:
        strips, total = ps.pop()
        key = ','.join(map(str, strips)) + f',{j}'
        
        cmx = dpg[key] if key in dpg else 0
        cmn = dpl[key] if key in dpl else float('inf')
        # print(cmx, cmn, total)
        cont = total >= cmx or total <= cmn

        if not cont: continue
        # for strips in [add_strips(strips, n) for n in range(-1,2)]:

        for i in range(slot_count):
            strips[i]+=turns[i]
            strips[i]%=len(a[i])
            # print(i, strips[i], a[i])
        result = [a[i][strips[i]] for i in range(slot_count)]
        muzzles = [a[i][strips[i]][1] for i in range(slot_count)]
        muzzles = ''.join(muzzles)
        oldr=result
        result = ''.join(result)

        # else:
        coins = 0
        # p_coins=[]
        for c in set(result):
            if c in muzzles: continue
            # if result.count(c)>2: p_coins += [result.count(c)-2]
            if result.count(c)>2: coins += result.count(c)-2
        # if p_coins: coins = sum(p_coins)
        # byte_coins_won += [coins]
        # dp[key] = coins
        total+=coins
        key = ','.join(map(str, strips)) + f',{j+1}'

        cmx = dpg[key] if key in dpg else 0
        cmn = dpl[key] if key in dpl else float('inf')
        # print(cmx, cmn, total)
        cont = total > cmx or total < cmn

        

        if not cont: continue

        if key in dpg: dpg[key] = max(total, dpg[key])
        else: dpg[key] = total
        if key in dpl: dpl[key] = min(total, dpl[key])
        else: dpl[key] = total

        if j+1 == l:
            ans_max = max(ans_max, total)
            ans_min = min(ans_min, total)
        # print(j+1, *oldr, total)

        for nstrips in [add_strips(strips, n) for n in range(-1,2)]: nps += [[list(nstrips), total]]
    
    ps=nps
    j+=1
# print(turns)


# get new input!!
# print(dpg, dpl)
print(ans_max, ans_min)
