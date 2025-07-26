dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]


def is_oob(coord, lines):
    r, c = coord
    return not (0 <= r < len(lines) and 0 <= c < len(lines[0]))


def check_xmas(coord, dir, lines):
    y, x = coord
    dr, dc = dir
    letters = ['X', 'M', 'A', 'S']

    for i, letter in enumerate(letters):
        ny = y + i * dr
        nx = x + i * dc
        if is_oob((ny, nx), lines):
            return False
        if lines[ny][nx] != letter:
            return False
    return True


lines = open('day04/0.in').read().splitlines()
total = 0
for r, line in enumerate(lines):
    for c, char in enumerate(line):
        for dir in dirs:
            if check_xmas((r, c), dir, lines):
                total += 1

print(total)
assert total == 2468
print('All tests pass.')
