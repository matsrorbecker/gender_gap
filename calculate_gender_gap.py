#!/usr/bin/env python3

import csv, sys, re
NUMBER_OF_PARTIES = 10

filename = sys.argv[1]

output = []

def to_float(str):
    return 0 if str == '..' else float(str)

with open(filename, newline='') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    age_group = re.search('(\d{2}-\d{2})|(\d{2}\+)', header_row[1]).group()
    first_row = True
    for row in reader:
        if first_row:
            start_month = row[0]
            first_row = False
        else:
            end_month = row[0]
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

with open(f"gender_gap_{age_group}yr_{start_month}-{end_month}.csv", 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    for row in output:
        writer.writerow(row)