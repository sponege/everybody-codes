
def min_max(nums):
    return min(nums), max(nums)
def print_board(board,ret=False):
    global minx, maxx, miny, maxy
    if len(board) > 0:
        minx, maxx = min_max([x for x, _ in board])
        miny, maxy = min_max([y for _, y in board])
    else:
        minx, maxx, miny, maxy = (0, 0, -1, 1)

    out = ''

    if ret:
        def pprint(*args, **kwargs):
            nonlocal out
            out += ''.join(map(str,args))
            if len(args) == 0:
                out += '\n'
            return out
    else:
        pprint = print
    pprint('\n')

    x_offset=max(len(str(-maxy+1)),len(str(-miny)))+2

    append_zeroes = lambda x: '0'*(len(str(maxx))-len(str(x)))+str(x)
    
    for digit in range(len(str(maxx))):
        pprint(' '*x_offset+' ', end='')
        for x in range(minx, maxx+1):
            pass
            pprint(append_zeroes(x)[digit], end='')
        pprint()

    pprint(' '*x_offset, end='')
    sand_drop_x = 500
    pprint()

    x_offset -= 2


    for y in range(miny-1, maxy+1):
        pprint(f"{(' '*(x_offset-len(str(y))))+str(y)} ", end='')
        for x in range(minx-1, maxx+2):
            c=board.get((x, y), '.')
            pprint(c if c!='^' else '.', end='')
        pprint()

    pprint()
    if ret:
        return out