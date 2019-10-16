KEYBOARD = [
    ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='],
    [None, 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']'],
    [None, 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", '\\'],
    [None, 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/']]
SHIFT_KEYBOARD = [
    ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+'],
    [None, 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}'],
    [None, 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"', '|'],
    [None, 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?']]

KEYBOARD_SET = set()
for li in KEYBOARD:
    for char in li:
        KEYBOARD_SET.add(char)

SHIFT_KEYBOARD_SET = set()
for li in SHIFT_KEYBOARD:
    for char in li:
        SHIFT_KEYBOARD_SET.add(char)


def find_distance(first_char, second_char):
    if first_char == ' ' or second_char == ' ':
        return 'Space Error'
    i1, j1 = get_location(first_char)
    i2, j2 = get_location(second_char)
    res = abs(i1 - i2) + abs(j1 - j2)
    if res > 100:
        return 'Invalid Key'
    return res


def get_location(c):
    if c in KEYBOARD_SET:
        for i, li in enumerate(KEYBOARD):
            for j, char in enumerate(li):
                if c == char:
                    return (i, j)
    if c in SHIFT_KEYBOARD_SET:
        for i, li in enumerate(SHIFT_KEYBOARD):
            for j, char in enumerate(li):
                if c == char:
                    return (i, j)
    else:
        return (999, 999)
