import sys
test = any('t' in arg for arg in sys.argv)

inp = open('08.inp1' if not test else '08.test').read()
lines = inp.splitlines()
br=5
buys=[]
priests = int(lines[0])
orig_blocks = 160 if test else 202400000  
blocks = orig_blocks
target = 1
i = 0
placed = 1
should = 0
thickness = 1
last = 0
acolytes =(5 if test else 1111)

heights=[1]
cumulative_heights=[1]

# mini=10000
maxi=20000
layer=0
# for layer in (range(4097) if test else range(maxi)):
while 1:

# while blocks > 0:
#     layer=i
    # for _ in range(layer):
        # print((thickness*priests)%(5 if test else 1111), thickness, priests)
    last = 0
    thickness = (thickness*priests)%acolytes
    thickness += acolytes
    target += 2
    old_placed = placed

    placed += thickness * target
    last = placed - old_placed
    blocks = orig_blocks - placed

    # print(thickness)
    # print(heights)
    # for j in range(len(heights)): heights[j] += thickness
    i += 1

    heights += [thickness]
    cumulative_heights += [thickness]
    # print(heights)

    # print(blocks, target-2, placed)
    # should = placed
    # blocks += target
    # placed -= target
    # target -= 2
    # print(last, old_placed, placed)
    # print(-blocks, ((i)*2)+1)
    # print(-blocks * (((i)*2)+1))
    layers=i+1
    remove = 0
    width = len(heights)-1
    width *= 2
    width += 1
    adds = []
    # print(cumulative_heights)
    for i in range(len(cumulative_heights)):
        if i != len(cumulative_heights)-1: cumulative_heights[i] += thickness
        # if not test and layer < mini: continue
        if blocks > 0 and not (layers > 11300 and layers <= 11327) and not test: continue
        # if blocks <= 0: continue
        # mul = 2 if i != 0 else 1
        add = priests * width
        add *= cumulative_heights[i]
        add %= acolytes
        # print(cumulative_heights)
        # print(priests, width, cumulative_heights[i], len(heights), add)
        # print(add)//273947
        # add *= mul
        adds += [add]
    if blocks > 0 and not (layers > 11300 and layers <= 11327) and not test: continue
    # adds=adds[::-1]
    # if test: print(adds, cumulative_heights)
    # removed = []
    # print(layer)
    # if blocks <= 0: continue
    # if not test and layer < mini: continue
    for i in range(len(adds) - 1):
        # if i > len(adds) - 2: continue
        # if i != len(adds)-1:# and adds[i] < heights[i+1]-1:
            # if test: print(adds[i])
        remove += adds[i] * (2 if i != 0 else 1)
        # else:
        #     print(adds[i])
        # removed += [remove]
    total = placed - remove
    buy = total - orig_blocks

    # print(heights)
    # print(cumulative_heights)
    # print(blocks)
    # print(placed, orig_blocks, remove)
    # print(total)
    # print(buy)
    if layers > 11300 and layers <= 11327:
        print(layers, total, buy)
    if buy > 0:
        buys += [buy]
        if not test: print(layers, total, buy, min(buys))
        br-=1
        if br == 0:break
    # if len(buys): print(min(buys))
    if test and layers < 10 or ((layers & (layer-1) == 0) and layers != 0 and layers%2==0):
        # print(adds)
        print(layers, total, buy)
    # print(layers)
    # print(buy)
    # print(layers)
    # print(layers)
    layer+=1
if not test: print(buys)
print(min(buys) if len(buys) else 'fuck')
