import os
import argparse
import csv
import numpy
import matplotlib
from matplotlib import pyplot, image


parser = argparse.ArgumentParser(description='Parameters required for processing.')

parser.add_argument('input-path', type=str, help='path to the csv input')


args = vars(parser.parse_args())

input_path = args['input-path']

with open(input_path) as f:
    reader = csv.reader(f)
    raw = list(reader)
    print(raw)
    # for row in reader:
    #     print(row)