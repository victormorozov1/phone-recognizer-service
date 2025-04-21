import os
from datetime import datetime

from lib.phone_recognition.data_load import load_from_files
from lib.phone_recognition.intervals_compressed_info import IntervalCompressedInfo


class PhonesDataLoader:
    def __init__(self, filenames: list[str]):
        self.filenames = filenames
        self._phones_data: IntervalCompressedInfo | None = None
        self._last_update_datetime: datetime | None = None

    def _get_update_datetime(self) -> datetime:
        max_datetime = None
        for filename in self.filenames:
            update_datetime_ts = os.path.getmtime(filename)
            update_datetime = datetime.fromtimestamp(update_datetime_ts)
            if max_datetime is None or update_datetime > max_datetime:
                max_datetime = update_datetime
        return max_datetime

    def get_phones_data(self) -> IntervalCompressedInfo:
        files_update_datetime = self._get_update_datetime()
        if files_update_datetime != self._last_update_datetime:
            self._phones_data = load_from_files(self.filenames)
            self._last_update_datetime = files_update_datetime
        return self._phones_data
