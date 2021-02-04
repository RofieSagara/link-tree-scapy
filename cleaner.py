from os import listdir, getcwd
from os.path import join
import time


def main():
    items_append = []
    content = join(getcwd(), 'content')
    data = join(content, 'data')
    result = join(content, 'result', 'result.txt')
    write_file = open(result, 'a', encoding='utf-8')

    items = listdir(data)
    start_time = time.time()
    for i in items:
        start_time_job = time.time()
        print('Start job with file ', i)
        file = open(join(data, i), 'r')
        lines = file.readlines()
        for line in lines:
            link = line.split(',', 1)[0]
            link = link.replace('https://', '').replace('http://', '')
            try:
                old_data = items_append.index(link)
                print('Data already insert skip it with index ', old_data, ' and value ', link)
            except ValueError:
                write_file.writelines(line)
                items_append.append(link)
        end_time_job = time.time()
        print('Done job with file ', i, ' with time ', end_time_job - start_time_job)
    end_time = time.time()
    print('All Job done with time ', end_time - start_time)
    write_file.close()


if __name__ == '__main__':
    main()
