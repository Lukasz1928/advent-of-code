import os
import re


def task_status(year, day, task):
    task_path = '{}/day{}/task{}'.format(year, str(day).zfill(2), task)
    if not os.path.isdir(task_path):
        return "notStated"
    if 'solution' not in os.listdir(task_path):
        return "inProgress"
    with open('{}/solution'.format(task_path)) as f:
        if len(f.read()) == 0:
            return "inProgress"
    return "solved"


icons = {
    'py': '<img src="https://img.icons8.com/color/48/000000/python.png">',
    'java': '<img src="https://img.icons8.com/color/48/000000/java-coffee-cup-logo.png"/>',
	'c': '<img src="https://img.icons8.com/color/48/000000/c-programming.png"/>',
	'icn': '<img src="https://www2.cs.arizona.edu/icon/wwwcube.gif" width="48" height="48"/>',
	'cpp': '<img src="https://img.icons8.com/color/48/000000/c-plus-plus-logo.png"/>'
}


#  assumes file exists
def get_solution_language_icon(year, day, task):
    try:
        task_path = '{}/day{}/task{}'.format(year, str(day).zfill(2), task)
        file = [f for f in os.listdir(task_path) if re.match(r'.+\..+', f)][0]
        ext = file.split('.')[-1]
    except Exception:
        return '<img src="https://img.icons8.com/color/48/000000/delete-sign.png"/>'
    try:
        return icons[ext]
    except KeyError:
        return '<img src="https://img.icons8.com/color/48/000000/checkmark.png"/>'


def task_sign(year, day, task):
    status = task_status(year, day, task)
    if status == "notStarted":
        return '<img src="https://img.icons8.com/color/48/000000/delete-sign.png"/>'
    elif status == "inProgress":
        return '<img src="https://img.icons8.com/color/48/000000/more.png"/>'
    return get_solution_language_icon(year, day, task)


def get_years_range():
    dir_content = [int(f) for f in os.listdir('.') if f.isnumeric()]
    return range(min(dir_content), max(dir_content) + 1)


def generate_table_header():
    thead = '<thead>\n\t<tr>\n\t\t<td colspan="2">Task\\Year</td>\n'
    for year in get_years_range():
        thead += '\t\t<td>{}</td>\n'.format(year)
    thead += '\t</tr>\n</thead>\n'
    return thead


def generate_table_body():
    tasks_count = 25
    years = get_years_range()

    table = '<tbody>\n'
    for tid in range(tasks_count):
        table += '\t<tr>'
        table += '\t\t<td rowspan="2">{}</td>\n'.format(str(tid + 1).zfill(2))
        table += "\t\t<td>1</td>\n"
        for year in years:
            table += '\t\t<td>{}</td>\n'.format(task_sign(year, tid + 1, 1))
        table += '\t</tr>'
        table += '\t<tr>'
        table += '\t\t<td>2</td>\n'
        for year in years:
            table += '\t\t<td>{}</td>\n'.format(task_sign(year, tid + 1, 2))
        table += '\t</tr>'
    table += '</tbody>\n'
    return table


def generate_solution_checklist_table():
    table = '<table>\n{}{}</table>'.format(generate_table_header(), generate_table_body())
    return table


def generate_icons_reference():
    ref = '<br>Most language icons obtained from <cite>[Icons8][2]</cite>'
    return ref


def main():
    text = "Solutions  of <cite>[Advent of Code][1]</cite> programming tasks."
    text += generate_solution_checklist_table()
    text += generate_icons_reference()
    text += "\n\n[1]: https://adventofcode.com/\n[2]: https://icons8.com/"
    with open('README.md', 'w+') as f:
        f.write(text)


if __name__ == "__main__":
    main()
