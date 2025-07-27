from pathlib import Path


def parse_input(filename):
    rules = []
    updates = []

    with open(Path(__file__).parent / filename) as file:
        for rule in file:
            if rule == '\n':
                break
            before, after = map(int, rule.split('|'))
            rules.append((before, after))

        for update in file:
            updates.append(list(map(int, update.split(','))))
        return rules, updates


def parse_file(filename):
    section1_lines = []
    section2_lines = []

    with open(filename, 'r') as file:
        # Process first section until blank line
        for line in file:
            line = line.strip()
            if line == '':
                break
            section1_lines.append((line))

        # Process remaining lines (second section)
        for line in file:
            line = line.strip()
            if line:  # skip any additional blank lines
                section2_lines.append((line))

    return section1_lines, section2_lines


def is_correctly_ordered(update, rules):
    position = {page: idx for idx, page in enumerate(update)}
    for before, after in rules:
        try:
            if position[before] > position[after]:
                return False
        except KeyError:
            continue
    return True


def get_middle_page(update):
    return update[len(update) // 2]


def count_correct_updates(rules, updates):
    total = 0
    for update in updates:
        if is_correctly_ordered(update, rules):
            total += get_middle_page(update)
    return total


def main():
    input_file = '0.in'

    correct_updates = count_correct_updates(*parse_input(input_file))

    print(f'{correct_updates}')
    assert correct_updates == 5452
    print('All tests pass.')


if __name__ == "__main__":
    main()
