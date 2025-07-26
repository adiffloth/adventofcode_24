from pathlib import Path


def is_in_bounds(coord, lines):
    r, c = coord
    return 0 <= r < len(lines) and 0 <= c < len(lines[0])


def matches_pattern(cells, lines):
    if all(is_in_bounds(cell, lines) for cell in cells):
        letters = [lines[x][y] for x, y in cells]
        return letters == ['M', 'A', 'S'] or letters == ['S', 'A', 'M']
    return False


def check_x_mas(r, c, lines):
    major = [(r-1, c-1), (r, c), (r+1, c+1)]
    minor = [(r-1, c+1), (r, c), (r+1, c-1)]
    return matches_pattern(major, lines) and matches_pattern(minor, lines)


def main():
    input_file = '0.in'
    lines = open(Path(__file__).parent / input_file).read().splitlines()
    total = 0
    for r in range(1, len(lines) - 1):  # Don't need to check first and last for center A
        for c in range(1, len(lines[0]) - 1):
            if lines[r][c] == 'A':
                if check_x_mas(r, c, lines):
                    total += 1
    print(f'{total}')
    assert total == 1864
    print('All tests pass.')


if __name__ == "__main__":
    main()
