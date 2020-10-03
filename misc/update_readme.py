import os
import re


def task_status(year, day, task, basedir):
    task_path = '{}/solutions/{}/day{}/task{}'.format(basedir, year, str(day).zfill(2), task)
    if not os.path.isdir(task_path):
        return "notStated"
    if 'solution' not in os.listdir(task_path):
        return "inProgress"
    with open('{}/solution'.format(task_path)) as f:
        if len(f.read()) == 0:
            return "inProgress"
    return "solved"

    
icons_order = ['py', 'java', 'c', 'cpp', 'hs', 'scala', 'kt', 'cs', 'rb', 'clj', 'erl', 'js', 'jl', 'r', 'm', 'fs', 'php', 'dart', 'lua', 'jy', 'go', 'rs', 'asm', 'sh', 'icn']

signs = {
    'solved': '<img src="misc/images/checkmark.png" width="48" height="48">',
    'unsolved': '<img src="misc/images/delete-sign.png" width="48" height="48">',
    'inprogress': '<img src="misc/images/more.png" width="48" height="48">'
}

sign_exceptions = {
    (2015, 25, 2): '<img src="misc/images/checkmark.png" width="48" height="48">',
    (2016, 25, 2): '<img src="misc/images/checkmark.png" width="48" height="48">',
    (2017, 25, 2): '<img src="misc/images/checkmark.png" width="48" height="48">'
}

#  assumes file exists
def get_solution_language_icon(year, day, task, basedir):
    try:
        task_path = '{}/solutions/{}/day{}/task{}'.format(basedir, year, str(day).zfill(2), task)
        file = [f for f in os.listdir(task_path) if re.match(r'.+\..+', f)][0]
        ext = file.split('.')[-1].lower()
    except Exception:
        return signs['unsolved']
        
    available_icons = os.listdir(basedir + '/misc/images')
    if (ext + '.png') in available_icons:
        return '<img src="misc/images/{}.png" width="48" height="48">'.format(ext)
    else:
        return signs['solved']


def task_sign(year, day, task, basedir):
    try:
        return sign_exceptions[(year, day, task)]
    except KeyError:
        pass # task not in sign_exceptions
    status = task_status(year, day, task, basedir)
    if status == "notStarted":
        return signs['unsolved']
    elif status == "inProgress":
        return signs['inprogress']
    return get_solution_language_icon(year, day, task, basedir)


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

def generate_languages_used_list(basedir):
    lst = "\n**LANGUAGES USED:**<br>\n"
    tasks_count = 25
    langs = set()
    for year in get_years_range(basedir):
        for task in range(tasks_count):
            for subtask in range(2):
                if task_status(year, task + 1, subtask + 1, basedir) == "solved":
                    langs.add(get_solution_language_icon(year, task + 1, subtask + 1, basedir))
    try:
        langs.remove(signs['solved'])
    except Exception:
        pass
    try:
        langs.remove(signs['unsolved'])
    except Exception:
        pass
    try:
        langs.remove(signs['inprogress'])
    except Exception:
        pass
    for i, l in enumerate(sorted(list(langs), key=lambda a: icons_order.index(a.split(' ')[1].split('/')[-1][:-5]))):
        if i > 0 and i % 5 == 0:
            lst += "<br>\n"
        lst += l
    lst += "<br>"
    return lst
    

def generate_solution_checklist_table(basedir):
    table = '<table>\n{}{}</table>'.format(generate_table_header(basedir), generate_table_body(basedir))
    return table


def main():
    wd = os.getcwd()
    basedir = '/'.join(wd.split('\\')[:-1]) if wd.endswith('misc') else wd
    text = "Solutions  of <cite>[Advent of Code][1]</cite> programming tasks.\n"
    text += generate_languages_used_list(basedir)
    text += generate_solution_checklist_table(basedir)
    text += "\n\n[1]: https://adventofcode.com/\n"
    with open(basedir + '\README.md', 'w+') as f:
        f.write(text)


if __name__ == "__main__":
    main()
