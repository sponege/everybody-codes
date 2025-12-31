import sys
test = any('t' in arg for arg in sys.argv)
inp = open('16.inp' if not test else '16.test').read()

ll = list(map(int, inp.split(',')))

ans = 0

# l2 = [0] * 6
target_blocks = 202520252025000
def get_blocks(length):
    cc = 0
    for n in ll:
        cc += length // n
        # c = -1
        # while c < length:
        #     if c >= 0: l2[c] += 1
        #     c += n
    return cc

u = 100000000000000000000000000
l = 1
while u > l + 1:
    m = ((u + l) // 2) + 1  
    if get_blocks(m) > target_blocks:
        u = m - 1
    else:
        l = m + 1

print(m, get_blocks(m), get_blocks(m-2), get_blocks(m+1))

# print(ans)
# print(','.join(map(str,l2)))
# print(sum(l2))