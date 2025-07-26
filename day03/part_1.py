import re

pattern = r"mul\(\d+,\d+\)"
total = 0
for line in open('AoC_24/day03/0.in', encoding='UTF-8').read().splitlines():
    matches = re.findall(pattern, line)
    for match in matches:
        a, b = match[4:-1].split(",")
        total += int(a) * int(b)
print(total)
assert total == 184122457
print('All tests pass.')
