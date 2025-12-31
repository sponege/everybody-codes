test = 0

inp = open('05.inp1' if not test else '05.test').read()
# inp2 = open('04.inp2' if not test else '04.test2').read()
# inp2 = open('03.inp1').read()
lines = [list(map(int,l.split())) for l in inp.splitlines()]

columns = [list(line) for line in zip(*lines)]

rounds = 10

# shouts = {}
shouts = set()

ans = 0

seen = set()

for round in range(9999999999):
    round_no=round
    round %= 4

    player = columns[round].pop(0)

    round += 1
    round %= 4

    # behind = player > len(columns[round])
    behind = ((player-1) // len(columns[round])) % 2 == 1
    index = player

    index %= len(columns[round])
    
    if behind:
        # print(index)
        index -= 1
        index %= len(columns[round])
        index = len(columns[round]) - index
        columns[round].insert(index, player)
    else: columns[round].insert(index-1, player)
    # else:
    #     columns[round].insert(player-1, player)

    # print(behind, round, index, player, columns)

    wow = ','.join([' '.join([str(c[j]) for c in columns]) for j in range(len(columns[0]))])
    if wow in seen: break
    seen.add(wow)

    shout = ''.join(str(c[0]) for c in columns)
    shout = int(shout)

    shouts.add(shout)

    # print(columns)
# print(max(shouts.keys()))
# print(sorted(list(shouts))
print(max(list(shouts)))
