test = 0

inp = open('04.inp1' if not test else '04.test').read()
# inp2 = open('04.inp2' if not test else '04.test2').read()
# inp2 = open('03.inp1').read()
nails = list(map(int,inp.splitlines()))

nails.sort()
# ans = sum(n - nails[0] for n in nails[1:])
strikes = []
for i in range(len(nails)):
    strikes += [sum(abs(n - nails[i]) for n in nails[i+1:] + nails[:i])]

print(strikes)
print(min(strikes))