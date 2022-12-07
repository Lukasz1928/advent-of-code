def read_input() -> list[list[str]]:
    with open('input', 'r') as f:
        return [list(group.strip().split('\n')) for group in f.read().split('$') if group]


files = {}
dirs = set()
data = read_input()
current_dir = '/'
for command in data:
    cmd, *out = command
    if cmd.startswith('cd'):
        location = cmd[3:]
        if location == '/':
            current_dir = '/'
        elif location == '..':
            current_dir = '/'.join(current_dir[:-1].split('/')[:-1]) + '/'
        else:
            current_dir = f'{current_dir}{location}/'
    else:
        for f in out:
            if not f.startswith('dir'):
                size, name = f.split(' ')
                files[f'{current_dir}{name}'] = int(size)

    dirs.add(current_dir)

sizes = {dir: sum(v for k, v in files.items() if k.startswith(dir)) for dir in dirs}

result = sum(v for v in sizes.values() if v < 100000)
print(result)
