from lib.phone_recognition.typings import PhoneNumbersInterval


class IntervalCompressedInfo:
    def __init__(self, data: list[PhoneNumbersInterval]):
        self.data = self._compress_data(data)

    @staticmethod
    def _compress_data(data: list[PhoneNumbersInterval]) -> list[PhoneNumbersInterval]:
        data.sort(key=lambda i: i.min_number)
        compressed_data = [data[0]]
        for interval in data:
            last = compressed_data[-1]
            if last.region == interval.region and last.operator == interval.operator:
                last.max_number = interval.max_number
            else:
                compressed_data.append(interval)
        return compressed_data

    def get_info(self, number: int) -> PhoneNumbersInterval | None:
        l, r = 0, len(self.data)
        while r - l > 1:
            m = (l + r) // 2
            if self.data[m].min_number <= number:
                l = m
            else:
                r = m
        if self.data[l].min_number <= number <= self.data[l].max_number:
            return self.data[l]
        return None
