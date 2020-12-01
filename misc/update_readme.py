import os
import re


def task_status(year, day, task, basedir):
    task_path = '{}/solutions/{}/day{}/task{}'.format(basedir, year, str(day).zfill(2), task)
    if not os.path.isdir(task_path):
        return "unsolved"
    files = os.listdir(task_path)
    if len(files) == 1 and files[0] == '.gitkeep':
        return "unsolved"
    if 'solution' not in os.listdir(task_path):
        return "inprogress"
    with open('{}/solution'.format(task_path)) as f:
        if len(f.read()) == 0:
            return "inprogress"
    return "solved"


signs = {
    'solved': '<img src="misc/images/solved.png" width="20" height="20">',
    'unsolved': '<img src="misc/images/notStarted.png" width="20" height="20">',
    'inprogress': '<img src="misc/images/inProgress.png" width="20" height="20">'
}

def read_sign_exceptions(basedir):
    d = basedir + '/misc'
    with open(d + '/exceptions', 'r') as f:
        exs = {tuple(int(x) for x in l.strip().split('-')) for l in f}
    return exs

def task_sign(year, day, task, basedir, exceptions):
    if (year, day, task) in exceptions:
        return signs['solved']
    status = task_status(year, day, task, basedir)
    return signs[status]


def get_years_range(basedir):
    return [int(f) for f in os.listdir(basedir + '/solutions') if f.isnumeric()]


def generate_table_header(basedir):
    thead = '<thead>\n\t<tr>\n\t\t<td></td>\n'
    for year in get_years_range(basedir):
        thead += '\t\t<td>{}</td>\n'.format(year)
    thead += '\t</tr>\n</thead>\n'
    return thead


def generate_table_body(basedir, exceptions):
    tasks_count = 25
    years = get_years_range(basedir)

    table = '<tbody>\n'
    for tid in range(tasks_count):
        table += '\t<tr>\n'
        table += '\t\t<td>day {}</td>\n'.format(str(tid + 1).zfill(2))
        for year in years:
            table += '\t\t<td><a href="solutions/{}/day{}/task{}">{}</a><a href="solutions/{}/day{}/task{}">{}</a></td>\n'.format(year, str(tid + 1).zfill(2), 1, task_sign(year, tid + 1, 1, basedir, exceptions), year, str(tid + 1).zfill(2), 2, task_sign(year, tid + 1, 2, basedir, exceptions))
        table += '\t</tr>\n'
    table += '</tbody>\n'
    return table
    

def generate_solution_checklist_table(basedir, exceptions):
    table = '<table>\n{}{}</table>'.format(generate_table_header(basedir), generate_table_body(basedir, exceptions))
    return table


def main():
    wd = os.getcwd()
    basedir = '/'.join(wd.split('\\')[:-1]) if wd.endswith('misc') else wd
    sign_exceptions = read_sign_exceptions(basedir)
    text = "Solutions  of <cite>[Advent of Code][1]</cite> programming tasks.\n"
    text += generate_solution_checklist_table(basedir, sign_exceptions)
    text += "\n\n[1]: https://adventofcode.com/\n"
    with open(basedir + '\README.md', 'w+') as f:
        f.write(text)


if __name__ == "__main__":
    main()
