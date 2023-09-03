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
        cancellation_code = row[22]
        if cancellation_code != 'NA':
            print(cancellation_code, 1)
