test = 0

inp = open('05.inp1' if not test else '05.test').read()
# inp2 = open('04.inp2' if not test else '04.test2').read()
# inp2 = open('03.inp1').read()
lines = [list(map(int,l.split())) for l in inp.splitlines()]

columns = [list(line) for line in zip(*lines)]

rounds = 10
for round in range(rounds):
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
        index = len(columns[round]) - (index-1)
        columns[round].insert(index, player)
    else: columns[round].insert(index-1, player)
    # else:
    #     columns[round].insert(player-1, player)

    # print(behind, round, index, player, columns)

print(''.join(str(c[0]) for c in columns))