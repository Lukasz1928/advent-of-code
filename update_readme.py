import os


def task_solved(year, day, task):
    task_path = '{}/day{}/task{}'.format(year, str(day).zfill(2), task)
    if not os.path.isdir(task_path):
        return False
    if 'main.py' not in os.listdir(task_path):
        return False
    return True


def task_sign(year, day, task):
    return "&#x2713" if task_solved(year, day, task) else "&#x2717"


def generate_table():
    table = '<table>\n<thead>\n\t<tr>\n\t\t<td rowspan="2">Day/Task</th>\n'
    for i in range(1, 26):
        table += '\t\t<td colspan="2" style="text-align:center;">{}</td>\n'.format(str(i).zfill(2))
    table += '\t</tr>\n\t<tr>\n'
    for i in range(1, 26):
        table += '\t\t<td>1</td>\n\t\t<td>2</td>\n'
    table += '\t</tr>\n</thead>\n<tbody>\n'
    years = ['2015', '2016', '2017', '2018', '2019']
    for year in years:
        year_row = '\t<tr>\n'
        year_row += '\t\t<td>{}</td>\n'.format(year)
        for day in range(1, 26):
            for task in range(1, 3):
                year_row += '\t\t\t<td>{}</td>\n'.format(task_sign(int(year), day, task))
        year_row += '\t</tr>\n'
        table += year_row
    table += '</tbody>\n</table>'
    return table


def main():
    text = "Solutions  of <cite>[Advent of Code][1]</cite> programming tasks."
    text += generate_table()
    text += "\n\n[1]: https://adventofcode.com/\n"
    with open('README.md', 'w') as f:
        f.write(text)


if __name__ == "__main__":
    main()
