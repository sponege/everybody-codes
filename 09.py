import sys
test = any('t' in arg for arg in sys.argv)

inp = open('09.inp1' if not test else '09.test').read()
lines = inp.splitlines()

stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]
stamps.sort(reverse=True)
print(stamps)
balls = list(map(int, lines))
a = 0

dp={}

for b in balls:
    beets=0
    ps = []
    minbeets = None
    seen=set()
    # for s in stamps:
    ps += [(b, 0, [])]
    z=0
    _ss=[]
    while len(ps)>0:
        # print(len(ps))
        type_beet=None
        b, c, ss = ps.pop()
        # if c in dp and b > dp[c]:
        #     # print(c, dp[c], b)
        #     continue
        # if c in dp: dp[c] = min(b, dp[c])
        # else: dp[c] = b 
        # print(b,c)
        if b <= 0:
            # print(b, c)
            if b == 0:
                if minbeets is None or c < minbeets: _ss = ss
                if minbeets is None: minbeets = c
                else: minbeets = min(minbeets, c)
            continue
        # next = None
        su = None
        for s in stamps:
            # s *= 775
            # if next is None and b-s>=0: next = b-s; su = s
            # if next is not None and b-s < next and b-s >= 0: type_beet=s; next = min(b-s, next); su = s
            if b-s < 0: continue
        # print("beetle type:",type_beet)
        # if next is None: continue
            next=b-s
            add=(next, c+1)
            if add in seen: continue
            # print(add)
            seen.add(add)
            ps += [(next, c+1, ss+[s])]
            # add=(next, c+1)
            # if add in seen: continue
            # seen.add(add)
            # ps += [(next, c+1, ss+[su])]
        z += 1
    # while b > 0:
    #     b -= cs
    #     beets+=1
    #     print(cs)
    print(minbeets, _ss)
    a += minbeets
    # print(beets)
print(a)