test = 0

inp = open('06.inp1' if not test else '06.test').read()
lines = inp.splitlines()
g = lines

nodes={}

for l in lines:
    node, destinations = l.split(':')
    destinations = destinations.split(',')
    nodes[node] = destinations

start = 'RR'
ps = [[start,0,start,'R']]

finished_ps=[]
visited=set()
# print(nodes)
while len(ps)>0:
    cur, l, path, cool_name = ps.pop()

    if cur == '@': finished_ps+=[[path,l,cool_name]]; continue


    if cur in visited: continue

    visited.add(cur)

    if cur not in nodes: continue


    for node in nodes[cur]:
        ps+=[[node,l+1,path+node+',',cool_name+node[0]]]
    # print(ps)
    
lengths=[p[1] for p in finished_ps]
    
finished_ps.sort(key=lambda l:l[1])
finished_ps.sort(key=lambda l:lengths.count(l[1]))

# print(finished_ps)
print(finished_ps[0])

print(sorted(lengths))