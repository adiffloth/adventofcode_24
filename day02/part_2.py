def is_ok_diff(diff):
    return 1 <= abs(diff) <= 3

def is_same_sign(dir, diff):
    return dir*diff > 0

def is_safe(levels):
    dir = levels[1] - levels[0]
    for i in range(len(levels) - 1):
        diff  = levels[i+1] - levels[i]
        if not is_ok_diff(diff) or not is_same_sign(dir, diff):
            return False
    return True

def is_safe_with_dampener(line):
    levels = [int(i) for i in line.split()]
    if is_safe(levels):
        return True

    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i + 1:]
        if is_safe(modified_levels):
            return True
    return False

s = sum([is_safe_with_dampener(line) for line in open('AoC_24/day02/0.in').read().splitlines()])
print(s)
assert s == 400
print('All tests pass.')
