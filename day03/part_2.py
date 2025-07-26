import re

mul_pattern = r"mul\((\d+),(\d+)\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"
total = 0
enabled = True
for line in open('day03/0.in').read().splitlines():
    tokens = re.split(r"(?<=\))", line)
    for token in tokens:
        if re.search(do_pattern, token):
            enabled = True
        elif re.search(dont_pattern, token):
            enabled = False
        else:
            match = re.search(mul_pattern, token)
            if match and enabled:
                a, b = map(int, match.groups())
                total += a * b

print(total)
assert total == 107862689
print('All tests pass.')
