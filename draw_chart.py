#!/usr/bin/env python3

import csv, sys
import matplotlib.pyplot as plt

filename = sys.argv[1]

x_data = []
y_data = []

with open(filename, newline='') as f:
    reader = csv.reader(f)
    next(reader) # skip header row
    for row in reader:
        x_data.append(row[0])
        y_data.append(float(row[2]))

plt.plot(x_data, y_data)
plt.xticks(rotation='vertical')
plt.show()