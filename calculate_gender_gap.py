#!/usr/bin/env python3

import csv, sys
NUMBER_OF_PARTIES = 10

filename = sys.argv[1]

output = []

def to_float(str):
    return 0 if str == '..' else float(str)

with open(filename, newline='') as f:
    reader = csv.reader(f)
    next(reader) # skip header row
    for row in reader:
        gender_gap = 0
        for i in range(1, NUMBER_OF_PARTIES + 1):
            support_from_men = to_float(row[i])
            support_from_women = to_float(row[i + NUMBER_OF_PARTIES])
            difference = abs(support_from_men - support_from_women)
            gender_gap += difference
        output.append([row[0], "{:.1f}".format(gender_gap)])

with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    for row in output:
        writer.writerow(row)