#!/usr/bin/env python3

import sys
import io

# Wrap sys.stdin in a TextIOWrapper with the desired encoding
input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8', errors='ignore')
# input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='latin-1')

# Input comes from STDIN (standard input)
for line in input_stream:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    row = line.split(',')

    if len(row) == 29:
        airline = row[8]

        try:
            arr_delay = float(row[14])
        except ValueError:
            continue

        try:
            dep_delay = float(row[15])
        except ValueError:
            continue

        on_schedule = 1 if arr_delay <= 15 and dep_delay <= 15 else 0
        print(airline, on_schedule, 1)
