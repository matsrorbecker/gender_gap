#!/usr/bin/env python3

import csv, sys
import matplotlib.pyplot as plt

filename = sys.argv[1]

x_data = []
y_data1 = []
y_data2 = []

with open(filename, newline='') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    x_label = header_row[0]
    y_label1 = header_row[1]
    y_label2 = header_row[2]
    for row in reader:
        x_data.append(row[0])
        y_data1.append(float(row[1]))
        y_data2.append(float(row[2]))

data = {}
data[x_label] = x_data
data[y_label1] = y_data1
data[y_label2] = y_data2

plt.plot(x_label, y_label1, y_label2, data=data)
plt.ylim(bottom=-1)
plt.xticks(rotation='vertical')
plt.legend([y_label1, y_label2])
plt.show()