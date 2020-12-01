import argparse
import os


def main():
    p = argparse.ArgumentParser()
    p.add_argument("-s", type=int, required=True)
    p.add_argument("-e", type=int, required=True)
    args = vars(p.parse_args())

    start_year = args['s']
    end_year = args['e']

    wd = os.getcwd()
    basedir = '/'.join(wd.split('\\')[:-1]) if wd.endswith('misc') else wd
    d = basedir + '/solutions'

    years_existing = {int(x) for x in os.listdir(d)}
    for year in range(start_year, end_year + 1):
        if year not in years_existing:
            os.makedirs(d + '/' + str(year))
        year_days = set(os.listdir(d + '/' + str(year)))
        for day in range(1, 26):
            day_directory = 'day{}'.format(str(day).zfill(2))
            if day_directory not in year_days:
                os.makedirs(d + '/' + str(year) + '/' + day_directory)
            day_tasks = set(os.listdir(d + '/' + str(year) + '/' + day_directory))
            for task in range(1, 3):
                task_directory = 'task' + str(task)
                if task_directory not in day_tasks:
                    os.makedirs(d + '/' + str(year) + '/' + day_directory + '/' + task_directory)
                dir_content = list(os.listdir(d + '/' + str(year) + '/' + day_directory + '/' + task_directory))
                if not dir_content:
                    f = open(d + '/' + str(year) + '/' + day_directory + '/' + task_directory + '/.gitkeep', 'w')
                    f.write('Task not yet started')


if __name__ == "__main__":
    main()
