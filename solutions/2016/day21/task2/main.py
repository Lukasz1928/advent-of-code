import re


def read_input():
    with open('input', 'r') as f:
        return [l.strip() for l in f]


def transform(password, command):
    match_swap_pos = re.match(r'swap position (\d+) with position (\d+)', command)
    if match_swap_pos is not None:
        p1, p2 = int(match_swap_pos.group(1)), int(match_swap_pos.group(2))
        password[p1], password[p2] = password[p2], password[p1]
        return password
    match_swap_let = re.match(r'swap letter (\w) with letter (\w)', command)
    if match_swap_let is not None:
        l1, l2 = match_swap_let.group(1), match_swap_let.group(2)
        p1, p2 = password.index(l1), password.index(l2)
        password[p1], password[p2] = password[p2], password[p1]
        return password
    match_rotate = re.match(r'rotate (left|right) (\d+) steps?', command)
    if match_rotate is not None:
        direction, steps = match_rotate.group(1), int(match_rotate.group(2)) % len(password)
        if direction == 'right':
            steps *= -1
        return password[-steps:] + password[:-steps]
    match_rotate_pos = re.match(r'rotate based on position of letter (\w)', command)
    if match_rotate_pos is not None:
        letter = match_rotate_pos.group(1)
        for l in range(len(password)):
            temp_password = password[l:] + password[:l]
            pos = temp_password.index(letter)
            rotation_length = (pos + (2 if pos >= 4 else 1)) % len(temp_password)
            if tuple(temp_password[-rotation_length:] + temp_password[:-rotation_length]) == tuple(password):
                return temp_password
    match_reverse = re.match(r'reverse positions (\d+) through (\d+)', command)
    if match_reverse is not None:
        p1, p2 = int(match_reverse.group(1)), int(match_reverse.group(2))
        password[p1:p2 + 1] = password[p1:p2 + 1][::-1]
        return password
    match_move = re.match(r'move position (\d+) to position (\d+)', command)
    if match_move is not None:
        p1, p2 = int(match_move.group(1)), int(match_move.group(2))
        letter = password[p2]
        password.remove(letter)
        return password[:p1] + [letter] + password[p1:]
    return None


def unscramble(password, commands):
    for c in reversed(commands):
        password = transform(password, c)
    return password


commands = read_input()
password = list("fbgdceah")
result = ''.join(unscramble(password, commands))
print(result)
