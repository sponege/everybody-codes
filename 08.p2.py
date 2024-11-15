import sys
test = any('t' in arg for arg in sys.argv)

inp = open('08.inp1' if not test else '08.test').read()
lines = inp.splitlines()

priests = int(lines[0])
orig_blocks = 50 if test else 20240000
blocks = orig_blocks
target = 1
i = 0
placed = 1
should = 0
thickness = 1
while blocks > 0:
    # print((thickness*priests)%(5 if test else 1111), thickness, priests)
    thickness = (thickness*priests)%(5 if test else 1111)
    target += 2
    placed += thickness * target
    blocks = orig_blocks - placed
    # print('p', placed, thickness, target, blocks)
    i += 1
    # print(blocks, target-2, placed)
# should = placed
# blocks += target
# placed -= target
# target -= 2
print(-blocks, ((i)*2)+1)
print(-blocks * (((i)*2)+1))