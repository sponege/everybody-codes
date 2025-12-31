import sys
test = any('t' in arg for arg in sys.argv)

inp = open('08.inp1' if not test else '08.test').read()
lines = inp.splitlines()

blocks = int(lines[0])

target = 1

placed = 0
should = 0

while blocks > 0:
    blocks -= target
    placed += target
    target += 2
    # print(blocks, target-2, placed)
# should = placed
# blocks += target
# placed -= target
# target -= 2

print((target - 2)* -blocks)