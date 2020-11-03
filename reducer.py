#!/usr/bin/env python3

import sys
current_time_stamp = None
current_count = 0
time_stamp = None
for line in sys.stdin:
    time_stamp, count = line.split('\t')
    try:
        count = int(count)
    except ValueError:
        continue
    if current_time_stamp == time_stamp:
        current_count += count
    else:
        if current_time_stamp:
            print(f'{current_time_stamp}\t{current_count}')
        current_count = count
        current_time_stamp = time_stamp
if current_time_stamp:
    print(f'{current_time_stamp}\t{current_count}')