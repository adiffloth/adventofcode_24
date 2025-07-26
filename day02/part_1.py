def is_ok_diff(diff):
    return 1 <= abs(diff) <= 3


def is_same_sign(dir, diff):
    return dir * diff > 0


def is_safe(line):
    levels = [int(i) for i in line.split()]
    dir = levels[1] - levels[0]
    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i]
        if not is_ok_diff(diff) or not is_same_sign(dir, diff):
            return False
    return True


s = sum([is_safe(line) for line in open('day02/0.in').read().splitlines()])
print(s)
assert s == 334
print('All tests pass.')
