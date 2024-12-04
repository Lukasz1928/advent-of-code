def read_input() -> list[str]:
    with open('input', 'r') as f:
        return [line.strip() for line in f]


def count_words(grid: list[str], start_location: tuple[int, int]) -> int:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    cnt = 0
    for direction in directions:
        for step, letter in enumerate('XMAS'):
            try:
                v, h = start_location[0] + step * direction[0], start_location[1] + step * direction[1]
                if v < 0 or h < 0:
                    break
                if grid[start_location[0] + step * direction[0]][start_location[1] + step * direction[1]] != letter:
                    break
            except IndexError:
                break
        else:
            cnt += 1
    return cnt


data = read_input()
count = 0
for vertical_start in range(len(data)):
    for horizontal_start in range(len(data[vertical_start])):
        count += count_words(data, (vertical_start, horizontal_start))
print(count)
