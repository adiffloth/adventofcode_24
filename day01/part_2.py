from collections import defaultdict

score = 0
ld, rd = defaultdict(int), defaultdict(int)
for line in open('day01/0.in').read().splitlines():
    l, r = (line.split())
    ld[l] += 1
    rd[r] += 1
for k in ld:
    score += int(k) * ld[k] * rd[k]
print(score)
assert score == 19457120
print('All tests pass.')
