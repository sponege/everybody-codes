import sys
test = any('t' in arg for arg in sys.argv)
rp = 1000
inp = (open('06.inp' if not test else '06.test').read())
lines = inp.strip().splitlines()
ans=0

dl = 1000

mc = [0] * 5
# for c in inp:
for i in range(0, (len(inp)*rp)+1):
    c = inp[i%len(inp)]
    if c in 'ABC':
        mc[ord(c)-ord('A')] += 1
    elif c in 'abc':
        ans += mc[ord(c)-ord('a')]
    if i >= dl:
        cc = inp[(i-dl)%len(inp)]
        if cc in 'ABC':
            mc[ord(cc)-ord('A')] -= 1

mc = [0] * 5
# for c in inp[::-1]:
for i in range((len(inp)*rp)-1, -1, -1):
    c = inp[i%len(inp)]
    if c in 'ABC':
        mc[ord(c)-ord('A')] += 1
    elif c in 'abc':
        ans += mc[ord(c)-ord('a')]
    if i <= (len(inp)*rp)-1-dl:
        cc = inp[(i+dl)%len(inp)]
        if cc in 'ABC':
            mc[ord(cc)-ord('A')] -= 1

print(ans)