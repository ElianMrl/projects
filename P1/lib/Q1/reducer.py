#!/usr/bin/env python3

import sys

current_airline = None
total_on_schedule = 0
total_flights = 0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    try:

        # parse the input from the mapper
        airline, on_schedule, count = line.split(" ")

        on_schedule = int(on_schedule)
        count = int(count)

    except ValueError:
        continue

    # this IF-switch only works because Hadoop sorts the map output
    # by key (here: airline) before it is passed to the reducer
    if current_airline == airline:
        total_on_schedule += on_schedule
        total_flights += count
    else:
        if current_airline:
            # write result to STDOUT
            print(current_airline, total_on_schedule/total_flights)
        total_on_schedule = on_schedule
        total_flights = count
        current_airline = airline

# do not forget to output the last word if needed!
if current_airline == airline:
    print(current_airline, total_on_schedule/total_flights)
