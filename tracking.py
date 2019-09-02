# python code that analyses csv files from an OS directory

import glob
import os

def count_rows(filename):
    with open(filename) as f:
        return sum(1 for line in f)

def avg_line(path, exclude_file):
    row_count = 0
    file_count = 0
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.csv' in file:
                filename = os.path.join(path, file)
                if filename != exclude_file:
                    rows = count_rows(filename)
                    row_count += rows
                    file_count += 1
    return row_count/file_count

def get_latest_file(path):
    list_of_files = glob.glob(path + '/*.csv')
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file

def main():
    dir = "./csv"
    latest_file = get_latest_file(dir)
    avg = avg_line(dir, latest_file)
    latest_rows = count_rows(latest_file)
    print("%d rows vs. %d rows" % (avg, latest_rows))


if __name__ == "__main__":
    main()
