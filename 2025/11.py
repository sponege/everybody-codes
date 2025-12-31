import sys
test = any('t' in arg for arg in sys.argv)
inp = open('11.inp' if not test else '11.test').read()
lines = inp.strip().splitlines()

birds = []
for i in lines:
    birds.append(int(i))

fp = 1
i = 0
while 1:
    # print(i, birds)
    # if fp:
    #     d = 0
    #     mr = 0
    #     for j in range(len(birds)-1):
    #         if birds[j] > 0 and birds[j] > birds[j+1]:
    #             s = birds[j] + birds[j+1]
    #             h = (s // 2)
    #             h2 = s - h
    #             mr = max(mr, max(abs(birds[j+1] - h), 1))
    #             birds[j] = h
    #             birds[j+1] = h2
    #             d = 1
    #     print(mr, birds)
    #     if d == 0:
    #         fp = 0
    #         print(birds)
    #     else:
    #         i += mr
    #     continue
    if fp:
        d = 0
        for j in range(len(birds)-1):
            if birds[j] > 0 and birds[j] > birds[j+1]:
                birds[j] -= 1
                birds[j+1] += 1
                d = 1
        if d == 0:
            fp = 0
            print(i, birds)
        else:
            i += 1
        continue
    mr = 0
    md = min(max(1, birds[j+1]-birds[j]) for j in range(len(birds)-1))
    for j in range(len(birds)-1):
        # print(md)
        if birds[j+1] > 0 and birds[j+1] > birds[j]:
            # s = birds[j] + birds[j+1]
            # h = (s // 2)
            # h2 = s - h
            birds[j] += md
            birds[j+1] -= md
    i += md
    # print(i)
    if md > 1: print('opitimization', md)
    birds.sort()
    if birds.count(birds[0]) == len(birds): break
print(i+1, birds)

ans = 0
# for i,v in enumerate(birds):
#     # print(i, v)
#     ans += (i+1) * v

print(i)