#!/usr/bin/env python3

import sys

current_cancellation_code = None
current_count = 0
cancellation_code = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    try:
        # parse the input from the mapper
        cancellation_code, count = line.split(" ")
        count = int(count)
    except ValueError:
        continue

    # this IF-switch only works because Hadoop sorts the map output
    # by key (here: airline) before it is passed to the reducer
    if current_cancellation_code == cancellation_code:
        current_count += count
    else:
        if current_cancellation_code:
            # write result to STDOUT
            print(current_cancellation_code,current_count)
        current_cancellation_code = cancellation_code
        current_count = count

# do not forget to output the last word if needed!
if current_cancellation_code == cancellation_code:
    print(current_cancellation_code,current_count)
