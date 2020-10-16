import re


def read_input():
    pts = []
    with open('input', 'r') as f:
        for line in f:
            m = re.match(r'Step (\w) must be finished before step (\w) can begin\.', line)
            pts.append((m.group(1), m.group(2)))
    return pts


class Task:
    def __init__(self, preconditions, name):
        self.preconditions = preconditions
        self.name = name
        self.required_time = (ord(name) - ord('A') + 1) + 60
        self.finished = False

    def can_be_started(self, done):
        for p in self.preconditions:
            if p not in done:
                return False
        return True

    def __hash__(self):
        return ord(self.name)


def make_tasks(order):
    names = set(x[0] for x in order) | set(x[1] for x in order)
    todo = {n: Task([], n) for n in names}
    for t in order:
        todo[t[1]].preconditions.append(t[0])
    return todo


def get_runnable_tasks(tasks, todo, done):
    return list(sorted([t for t in todo if (not tasks[t].finished) and tasks[t].can_be_started(done)]))


def run(tasks, workers):
    todo = set([t.name for t in tasks.values()])
    done = set()
    in_progress = set()
    spare_workers = workers
    runnable = get_runnable_tasks(tasks, todo, done)
    time = 0
    while len(todo) + len(in_progress) > 0:
        while spare_workers > 0 and len(runnable) > 0:
            new_task = runnable.pop(0)
            in_progress.add(new_task)
            todo.remove(new_task)
            spare_workers -= 1
        still_in_progress = set()
        for task_name in in_progress:
            task = tasks[task_name]
            task.required_time -= 1
            if task.required_time == 0:
                task.finished = True
                done.add(task_name)
                spare_workers += 1
            else:
                still_in_progress.add(task_name)
        in_progress = still_in_progress
        runnable = get_runnable_tasks(tasks, todo, done)
        time += 1
    return time


raw_order = read_input()
tasks = make_tasks(raw_order)
result = run(tasks, 5)
print(result)
