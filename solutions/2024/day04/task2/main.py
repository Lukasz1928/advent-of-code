def read_input() -> list[str]:
    with open('input', 'r') as f:
        return [line.strip() for line in f]


def is_mas_cross(grid: list[str], start_location: tuple[int, int]) -> bool:
    if grid[start_location[0]][start_location[1]] != 'A':
        return False
    return (
        {grid[start_location[0] - 1][start_location[1] - 1], grid[start_location[0] + 1][start_location[1] + 1]} == {'M', 'S'} and
        {grid[start_location[0] + 1][start_location[1] - 1], grid[start_location[0] - 1][start_location[1] + 1]} == {'M', 'S'}
    )


data = read_input()
count = 0
for vertical_start in range(1, len(data) - 1):
    for horizontal_start in range(1, len(data[vertical_start]) - 1):
        if is_mas_cross(data, (vertical_start, horizontal_start)):
            count += 1
print(count)
