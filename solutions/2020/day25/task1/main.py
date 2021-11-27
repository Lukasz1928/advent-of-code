
def read_input():
    with open('input', 'r') as f:
        return tuple(int(line.strip()) for line in f.readlines())


def transform_step(value, subject_number):
    return (value * subject_number) % 20201227


def transform(subject_number, count):
    value = 1
    for _ in range(count):
        value = transform_step(value, subject_number)
    return value


def find_loop_size(public_key, subject_number=7):
    value = 1
    ls = 0
    while value != public_key:
        value = transform_step(value, subject_number)
        ls += 1
    return ls


card_key, door_key = read_input()
door_loop_size = find_loop_size(door_key)
result = transform(card_key, door_loop_size)
print(result)
