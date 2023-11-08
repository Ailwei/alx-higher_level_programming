#!/usr/bin/python3
"""
yeah
"""


import sys
import signal


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

total_file_size = 0
line_count = 0


def handle_interrupt(signum, frame):
    """
    Signal handler for KeyboardInterrupt (Ctrl+C).
    Prints the metrics and exits gracefully.
    """

    print_metrics()
    sys.exit(0)


def print_metrics():
    """
    Prints the accumulated metrics including the total file size
    and status code counts.
    """
    print(f"Total file size: {total_file_size}")
    for status_code in sorted(metrics.keys()):
        count = metrics[status_code]
        if count > 0:
            print(f"{status_code}: {count}")


signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        line_count += 1
        try:
            parts = line.split()
            status_code = parts[-2]
            file_size = int(parts[-1])
            total_file_size += file_size

            if status_code in metrics:
                metrics[status_code] += 1
        except (IndexError, ValueError):
            pass

        if line_count % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    handle_interrupt(None, None)
