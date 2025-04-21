import csv
from typing import Iterable

from lib.phone_recognition.interval_map import IntervalMap
from lib.phone_recognition.typings import PhoneNumbersInterval


def load_from_files(files: Iterable[str]) -> IntervalMap:
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

    return IntervalMap(intervals)
