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
	'rs': '<img src="https://www.rust-lang.org/logos/rust-logo-blk.svg" width="48" height="48"/>',
	'erl': '<img src="https://img.icons8.com/windows/64/000000/erlang.png" width="48" height="48"/>',
	'lua': '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Lua-Logo.svg/1024px-Lua-Logo.svg.png" width="48" height="48"/>',
    'asm': '<img src="https://i.pinimg.com/236x/8c/b1/8c/8cb18c72082d13eb581cf6d452e8e266.jpg" widht="48" height="48"/>',
	'kt': '<img src="https://img.icons8.com/color/48/000000/kotlin.png"/>',
	'go': '<img src="https://img.icons8.com/color/48/000000/golang.png"/>',
    'lisp': '<img src="https://img.icons8.com/color/48/000000/lisp.png"/>',
    'm': '<img src="https://download.logo.wine/logo/GNU_Octave/GNU_Octave-Logo.wine.png" width="48" height="48"/>',
    'clj': '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Clojure_logo.svg/1024px-Clojure_logo.svg.png" width="48" height="48"/>',
    'fs': '<img src="https://fsharp.org/img/logo/fsharp256.png" width="48" height="48"/>',
    'dart': '<img src="https://cdn.freebiesupply.com/logos/thumbs/2x/dart-logo.png" width="48" height="48">',
    'jy' : '<img src="https://blog.xebialabs.com/wp-content/uploads/2016/02/logo6.gif" width="48" height="48"/>',
    'icn': '<img src="https://www2.cs.arizona.edu/icon/wwwcube.gif" width="48" height="48"/>',
}

signs = {
    'solved': '<img src="https://img.icons8.com/color/48/000000/checkmark.png"/>',
    'unsolved': '<img src="https://img.icons8.com/color/48/000000/delete-sign.png"/>',
    'inprogress': '<img src="https://img.icons8.com/color/48/000000/more.png"/>'
}

sign_exceptions = {
    (2015, 25, 2): '<img src="https://img.icons8.com/color/48/000000/checkmark.png"/>',
    (2017, 25, 2): '<img src="https://img.icons8.com/color/48/000000/checkmark.png"/>'
}

#  assumes file exists
def get_solution_language_icon(year, day, task, basedir):
    try:
        task_path = '{}/solutions/{}/day{}/task{}'.format(basedir, year, str(day).zfill(2), task)
        file = [f for f in os.listdir(task_path) if re.match(r'.+\..+', f)][0]
        ext = file.split('.')[-1]
    except Exception:
        return signs['unsolved']
    try:
        return icons[ext]
    except KeyError:
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
                print(task_status(year, task + 1, subtask + 1, basedir))
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
    for i, l in enumerate(sorted(list(langs), key=lambda a: list(icons.values()).index(a))):
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
