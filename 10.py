import sys
test = any('t' in arg for arg in sys.argv)

inp = open('10.inp1' if not test else '10.test').read()
lines = inp.splitlines()

tsm = {}
tss=[]
for l in lines:
    t1, rt = l.split(':')
    rt = rt.split(',')
    tsm[t1] = rt
    tss.append(t1)

def h(ct):
    return ','.join(map(str, ct))
dp={}
def getlen(ct, n):
    # print(ct, n)
    _h=h(ct+[n])
    if _h in dp: return dp[_h]
    if n == 0: return len(ct)
    thing = sum(getlen(tsm[t], n-1) for t in ct)
    dp[_h] = thing
    return thing

vals=[]
for st in tss:
    ts = [st]
    val=getlen(ts, 20)
    vals.append(val)
print(dp)

print(vals)
print(max(vals) - min(vals))