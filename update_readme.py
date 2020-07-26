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
    'cpp': '<img src="https://img.icons8.com/color/48/000000/c-plus-plus-logo.png"/>',
	'hs': '<img src="https://img.icons8.com/material/48/000000/haskell.png"/>',
	'scala': '<img src="https://img.icons8.com/dusk/64/000000/scala.png" width="48" height="48"/>',
	'sh': '<img src="https://img.icons8.com/fluent/48/000000/console.png"/>',
	'R': '<img src="https://www.r-project.org/logo/Rlogo.png" width="48" height="48"/>',
	'cs': '<img src="https://img.icons8.com/color/48/000000/c-sharp-logo-2.png"/>',
	'php': '<img src="https://img.icons8.com/officel/80/000000/php-logo.png" width="48" height="48"/>',
	'js': '<img src="https://img.icons8.com/color/48/000000/javascript.png"/>',
	'jl': '<img src="https://symbols.getvecta.com/stencil_85/50_julia-language-icon.d9f53761e1.svg" width="48" height="48"/>',
	'rb': '<img src="https://img.icons8.com/color/48/000000/ruby-programming-language.png"/>',
	'rs': '<img src="<img src="https://www.rust-lang.org/logos/rust-logo-blk.svg"/>" width="48" height="48"/>',
	'erl': '<img src="https://img.icons8.com/windows/64/000000/erlang.png" width="48" height="48"/>',
	'lua': '<img src="https://en.wikipedia.org/wiki/Lua_(programming_language)#/media/File:Lua-Logo.svg" width="48" height="48"/>',
    'asm': '<img src="http://abolfazlm.com/image/Assembly-logo.png" widht="48" height="48"/>',
	'kt': '<img src="https://img.icons8.com/color/48/000000/kotlin.png"/>',
	'go': '<img src="https://img.icons8.com/color/48/000000/golang.png"/>',
    'lisp': '<img src="https://img.icons8.com/color/48/000000/lisp.png"/>',
    'icn': '<img src="https://www2.cs.arizona.edu/icon/wwwcube.gif" width="48" height="48"/>',
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
        table += '\t<tr>\n'
        table += '\t\t<td rowspan="2">{}</td>\n'.format(str(tid + 1).zfill(2))
        table += "\t\t<td>1</td>\n"
        for year in years:
            table += '\t\t<td>{}</td>\n'.format(task_sign(year, tid + 1, 1))
        table += '\t</tr>\n'
        table += '\t<tr>\n'
        table += '\t\t<td>2</td>\n'
        for year in years:
            table += '\t\t<td>{}</td>\n'.format(task_sign(year, tid + 1, 2))
        table += '\t</tr>\n'
    table += '</tbody>\n'
    return table

def genrate_languages_used_list():
    lst = "\n**LANGUAGES USED:**<br>\n"
    tasks_count = 25
    langs = set()
    for year in get_years_range():
        for task in range(tasks_count):
            for subtask in range(2):
                if task_status(year, task + 1, subtask + 1) == "solved":
                    langs.add(get_solution_language_icon(year, task + 1, subtask + 1))
    try:
        langs.remove('<img src="https://img.icons8.com/color/48/000000/checkmark.png"/>')
    except Exception:
        pass
    try:
        langs.remove('<img src="https://img.icons8.com/color/48/000000/delete-sign.png"/>')
    except Exception:
        pass
    try:
        langs.remove('<img src="https://img.icons8.com/color/48/000000/more.png"/>')
    except Exception:
        pass
    for i, l in enumerate(sorted(list(langs), key=lambda a: list(icons.values()).index(a))):
        if i > 0 and i % 10 == 0:
            lst += "<br>\n"
        lst += l
    lst += "<br>"
    return lst
    

def generate_solution_checklist_table():
    table = '<table>\n{}{}</table>'.format(generate_table_header(), generate_table_body())
    return table


def main():
    text = "Solutions  of <cite>[Advent of Code][1]</cite> programming tasks.\n"
    text += genrate_languages_used_list()
    text += generate_solution_checklist_table()
    text += "\n\n[1]: https://adventofcode.com/\n"
    with open('README.md', 'w+') as f:
        f.write(text)


if __name__ == "__main__":
    main()
