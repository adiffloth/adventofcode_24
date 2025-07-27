# Some weird change
from pathlib import Path


def main():
    input_file = '0.in'
    lines = open(Path(__file__).parent / input_file).read().splitlines()

    print(f'{len(lines)}')
    assert len(lines) == 1000
    print('All tests pass.')


if __name__ == "__main__":
    main()
