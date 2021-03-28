#!/usr/bin/env python3

import csv, sys
import matplotlib.pyplot as plt

filename = sys.argv[1]

data = {}

with open(filename, newline='') as f:
    reader = csv.reader(f)
    labels = next(reader)
    x_label = labels[0]
    for label in labels:
        data[label] = []
    for row in reader:
        data[x_label].append(row[0])
        for i in range(1, len(labels)):
            data[labels[i]].append(float(row[i]))

for i in range(1, len(labels)):
    plt.plot(data[x_label], data[labels[i]])

plt.ylim(bottom=-1)
plt.xticks(rotation='vertical')
plt.legend(labels[1:len(labels)])
plt.show()