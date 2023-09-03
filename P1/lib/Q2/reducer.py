#!/usr/bin/env python3

import sys

current_airline = None
total_in_taxi_time = 0
total_out_taxi_time = 0
total_in_flights = 0
total_out_flights = 0

print('airline', 'In', 'Out')

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    try:
        # parse the input from the mapper
        airline, direction, taxi_time, count = line.split(" ")

        taxi_time = float(taxi_time)
        count = int(count)
    except ValueError:
        continue

    # this IF-switch only works because Hadoop sorts the map output
    # by key (here: airline) before it is passed to the reducer
    if current_airline == airline:
        if direction == 'in':
            total_in_taxi_time += taxi_time
            total_in_flights += count
        elif direction == 'out':
            total_out_taxi_time += taxi_time
            total_out_flights += count

    else:
        if current_airline:
            if total_in_flights == 0:
                print(current_airline, 'No in Flights', total_out_taxi_time / total_out_flights)
            elif total_out_flights == 0:
                print(current_airline, total_in_taxi_time / total_in_flights, 'No out Flights')
            elif total_in_flights == 0 and total_out_flights == 0:
                print(current_airline, 'No Flights')
            else:
                print(current_airline, total_in_taxi_time / total_in_flights, total_out_taxi_time / total_out_flights)

        current_airline = airline
        if direction == 'in':
            total_in_taxi_time = taxi_time
            total_in_flights = count
        elif direction == 'out':
            total_out_taxi_time = taxi_time
            total_out_flights = count


# do not forget to output the last word if needed!
if current_airline == airline:
    if total_in_flights == 0:
        print(current_airline, 'No in Flights', total_out_taxi_time / total_out_flights)
    elif total_out_flights == 0:
        print(current_airline, total_in_taxi_time / total_in_flights, 'No out Flights')
    elif total_in_flights == 0 and total_out_flights == 0:
        print(current_airline, 'No Flights')
    else:
        print(current_airline, total_in_taxi_time / total_in_flights, total_out_taxi_time / total_out_flights)
