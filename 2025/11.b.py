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
    if fp:
        d = 0
        for j in range(len(birds)-1):
            if birds[j] > 0 and birds[j] > birds[j+1]:
                birds[j] -= 1
                birds[j+1] += 1
                d = 1
        if d == 0:
            fp = 0
            print(birds)
        else:
            i += 1
        continue

    for j in range(len(birds)-1):
        if birds[j+1] > 0 and birds[j+1] > birds[j]:
            birds[j+1] -= 1
            birds[j] += 1
    i += 1
    if birds.count(birds[0]) == len(birds): break
print(i+1, birds)

ans = 0
# for i,v in enumerate(birds):
#     # print(i, v)
#     ans += (i+1) * v

print(i)