lt, rt = [], []
for line in open('day01/0.in').read().splitlines():
    l, r = (line.split())
    lt.append(int(l))
    rt.append(int(r))
s = 0
for l, r in zip(sorted(lt), sorted(rt)):
    s += abs(l - r)
print(s)
assert s == 2264607
print('All tests pass.')
