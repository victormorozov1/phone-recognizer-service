import os
from datetime import datetime

from lib.phone_recognition.interval_map import IntervalMap
from lib.phone_recognition.load import load_from_files


class PhonesDataLoader:
    def __init__(self, phones_data_filenames: list[str]):
        self.phones_data_filenames = phones_data_filenames
        self._phones_data: IntervalMap | None = None
        self._last_update_datetime: datetime | None = None

    def _get_update_datetime(self) -> datetime:
        max_datetime = None
        for filename in self.phones_data_filenames:
            update_datetime_ts = os.path.getmtime(filename)
            update_datetime = datetime.fromtimestamp(update_datetime_ts)
            if max_datetime is None or update_datetime > max_datetime:
                max_datetime = update_datetime
        return max_datetime

    def get_phones_data(self) -> IntervalMap:
        files_update_datetime = self._get_update_datetime()
        if files_update_datetime != self._last_update_datetime:
            self._phones_data = load_from_files(self.phones_data_filenames)
            self._last_update_datetime = files_update_datetime
        return self._phones_data
