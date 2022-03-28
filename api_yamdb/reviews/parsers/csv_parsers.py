import csv
import sys

DIR = sys.path[0] + '/static/data/'


def csv_parse(filename):
    csv_path = DIR + filename + '.csv'
    fields_list = []
    try:
        with open(csv_path, 'r', newline='') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                fields_list.append(row)
        return fields_list
    except FileNotFoundError:
        return None
