import os
import re


def task_status(year, day, task, basedir):
    task_path = '{}/solutions/{}/day{}/task{}'.format(basedir, year, str(day).zfill(2), task)
    if not os.path.isdir(task_path):
        return "unsolved"
    if 'solution' not in os.listdir(task_path):
        return "inprogress"
    with open('{}/solution'.format(task_path)) as f:
        if len(f.read()) == 0:
            return "inprogress"
    return "solved"


signs = {
    'solved': '<img src="misc/images/solved.png" width="48" height="48">',
    'unsolved': '<img src="misc/images/notStarted.png" width="48" height="48">',
    'inprogress': '<img src="misc/images/inProgress.png" width="48" height="48">'
}

sign_exceptions = {
    (2015, 25, 2): '<img src="misc/images/solved.png" width="48" height="48">',
    (2016, 25, 2): '<img src="misc/images/solved.png" width="48" height="48">',
    (2017, 25, 2): '<img src="misc/images/solved.png" width="48" height="48">'
}


def task_sign(year, day, task, basedir):
    try:
        return sign_exceptions[(year, day, task)]
    except KeyError:
        pass # task not in sign_exceptions
    status = task_status(year, day, task, basedir)
    return signs[status]


def get_years_range(basedir):
    dir_content = [int(f) for f in os.listdir(basedir + '/solutions') if f.isnumeric()]
    return range(min(dir_content), max(dir_content) + 1)


def generate_table_header(basedir):
    thead = '<thead>\n\t<tr>\n\t\t<td colspan="2">Task\\Year</td>\n'
    for year in get_years_range(basedir):
        thead += '\t\t<td>{}</td>\n'.format(year)
    thead += '\t</tr>\n</thead>\n'
    return thead


def generate_table_body(basedir):
    tasks_count = 25
    years = get_years_range(basedir)

    table = '<tbody>\n'
    for tid in range(tasks_count):
        table += '\t<tr>\n'
        table += '\t\t<td rowspan="2">{}</td>\n'.format(str(tid + 1).zfill(2))
        table += "\t\t<td>1</td>\n"
        for year in years:
            table += '\t\t<td>{}</td>\n'.format(task_sign(year, tid + 1, 1, basedir))
        table += '\t</tr>\n'
        table += '\t<tr>\n'
        table += '\t\t<td>2</td>\n'
        for year in years:
            table += '\t\t<td>{}</td>\n'.format(task_sign(year, tid + 1, 2, basedir))
        table += '\t</tr>\n'
    table += '</tbody>\n'
    return table
    

def generate_solution_checklist_table(basedir):
    table = '<table>\n{}{}</table>'.format(generate_table_header(basedir), generate_table_body(basedir))
    return table


def main():
    wd = os.getcwd()
    basedir = '/'.join(wd.split('\\')[:-1]) if wd.endswith('misc') else wd
    text = "Solutions  of <cite>[Advent of Code][1]</cite> programming tasks.\n"
    text += generate_solution_checklist_table(basedir)
    text += "\n\n[1]: https://adventofcode.com/\n"
    with open(basedir + '\README.md', 'w+') as f:
        f.write(text)


if __name__ == "__main__":
    main()
