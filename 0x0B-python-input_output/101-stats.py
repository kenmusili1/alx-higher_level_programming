#!/usr/bin/python3
"""represent function that reads from standard input and computes metrics."""

import signal
import sys


def print_metrics(total_size, status_codes):
    """Print accumulated metrics."""

    print("File size: {}".format(total_size))
    for status_code in sorted(status_codes.keys()):
        if status_codes[status_code] > 0:
            print("{}: {}".format(status_code, status_codes[status_code]))

def signal_handler(signum, frame):
    global total_size, status_codes
    print_metrics(total_size, status_codes)
    sys.exit(0)

def main():
    global total_size, status_codes
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    signal.signal(signal.SIGINT, signal_handler)

    for line in sys.stdin:
        line = line.strip().split()
        if len(line) > 6:
            status_code = int(line[-2])
            file_size = int(line[-1])
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1

        line_count += 1

        if line_count % 10 == 0:
            print_metrics(total_size, status_codes)

if __name__ == "__main__":
    main()
