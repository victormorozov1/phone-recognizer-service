import csv
from typing import Iterable

from lib.phone_recognition.intervals_compressed_info import IntervalCompressedInfo
from lib.phone_recognition.typings import PhoneNumbersInterval


def load_from_files(files: Iterable[str]) -> IntervalCompressedInfo:
    intervals: list[PhoneNumbersInterval] = []
    for filename in files:
        with open(filename) as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            next(reader)  # Skip headers
            for row in reader:
                min_number = int(row[0] + row[1])
                max_number = int(row[0] + row[2])
                operator = row[4]
                region = row[5]
                interval = PhoneNumbersInterval(
                    min_number=min_number,
                    max_number=max_number,
                    operator=operator,
                    region=region,
                )
                intervals.append(interval)

    return IntervalCompressedInfo(intervals)


if __name__ == '__main__':
    op, re = load_from_files(
        [
            '/Users/viktor/Documents/ABC-3xx.csv',
            '/Users/viktor/Documents/ABC-4xx.csv',
            '/Users/viktor/Documents/ABC-8xx.csv',
            '/Users/viktor/Documents/DEF-9xx.csv',
        ],
    )
    print(len(re))
