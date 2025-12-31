import sys
test = any('t' in arg for arg in sys.argv)

inp = open('04.inp' if not test else '04.test').read()
lines = inp.splitlines()

# t=int(lines[0])*100
o = int(lines[0])*100
t = 1
for i in lines[1:-1]:
    a, b = map(int, i.split('|'))
    
    t *= (o/a)
    o = b
t *= o/int(lines[-1])
import math
t = math.floor(t)
print(t)