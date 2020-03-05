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
    # gaze_data = []
    # sample_array = []
    # array = [1,2,3]
    # array2 = [4,5,6]
    # sample_array.append(array)
    # sample_array.append(array2)
    # sample_list = []
    # sample_list = list(map(lambda q: (int(q[0]), int(q[1]), 1), sample_array))
    # if len(raw[0]) is 2:
    #     gaze_data = list(map(lambda q: (int(q[0]), int(q[1]), 1), raw))
    # else:
    #     gaze_data =  list(map(lambda q: (int(q[0]), int(q[1]), int(q[2])), raw))
    # print(gaze_data)
    # print(sample_list)
    # for row in reader:
    #     print(row)