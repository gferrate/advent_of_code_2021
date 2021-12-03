import csv


def read_csv(fn):
    with open(fn, 'r') as f:
        reader = csv.reader(f, delimiter=' ')
        return list(reader)
