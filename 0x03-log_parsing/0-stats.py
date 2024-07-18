#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""

import sys


# Dictionary to store the count of all status codes
status_codes_dict = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_size = 0
count = 0  # Keeps track of the number of lines processed


def print_stats():
    """Prints the accumulated statistics"""
    print(f'File size: {total_size}')
    for code in sorted(status_codes_dict.keys()):
        if status_codes_dict[code] > 0:
            print(f'{code}: {status_codes_dict[code]}')


try:
    for line in sys.stdin:
        parts = line.split()

        if len(parts) >= 7:
            status_code = parts[-2]
            file_size = parts[-1]

            # Validate and update the status code count
            if status_code.isdigit():
                status_code = int(status_code)
                if status_code in status_codes_dict:
                    status_codes_dict[status_code] += 1

            # Validate and update the total file size
            if file_size.isdigit():
                total_size += int(file_size)

            # Update line count and print stats every 10 lines
            count += 1
            if count == 10:
                print_stats()
                count = 0  # Reset line count

except Exception as err:
    pass

finally:
    print_stats()  # Print final stats
