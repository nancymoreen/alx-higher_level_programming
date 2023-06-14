#!/usr/bin/python3
"""Module for reading stdin and computing metrics
"""
import sys


metrics = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
        }
total_size = 0
counter = 0

try:
    for line in sys.stdin:
        counter += 1
        split_line = line.split(" ")
        if len(split_line) > 2:
            status_code = split_line[-2]
            file_size = split_line[-1]
            if status_code in metrics:
                metrics[status_code] += 1
                total_size += int(file_size)
                if counter % 10 == 0:
                    print("File size: {}".format(total_size))
                    for status, count in sorted(metrics.items()):
                        if count != 0:
                            print("{}: {}".format(status, count))

except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for status, count in sorted(metrics.items()):
        if count != 0:
            print("{}: {}".format(status, count))
