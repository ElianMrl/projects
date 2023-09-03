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
        airline_origin = row[16]
        airline_destin = row[17]

        try:
            taxi_in = float(row[19])
        except ValueError:
            continue

        try:
            taxi_out = float(row[20])
        except ValueError:
            continue

        print(airline_origin, 'out', taxi_out, 1)
        print(airline_destin, 'in', taxi_in, 1)