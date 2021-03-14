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
        gender_gap1 = 0 # sum of all differences
        gender_gap2 = 0 # sum of all significant (at 95% level) differences
        for i in range(1, NUMBER_OF_PARTIES + 1):
            support_from_men = to_float(row[i])
            support_from_women = to_float(row[i + NUMBER_OF_PARTIES])
            difference = abs(support_from_men - support_from_women)
            gender_gap1 += difference
            error_margin_men = to_float(row[i + NUMBER_OF_PARTIES * 2])
            error_margin_women = to_float(row[i + NUMBER_OF_PARTIES * 3])
            if difference - error_margin_men - error_margin_women > 0:
                gender_gap2 += difference
        output.append([row[0], "{:.1f}".format(gender_gap1), "{:.1f}".format(gender_gap2)])

with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    for row in output:
        writer.writerow(row)