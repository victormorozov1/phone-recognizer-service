from typing import Literal

from lib.phone_recognition.errors import UnknownCountryCode
from lib.phone_recognition.intervals_compressed_info import IntervalCompressedInfo


def get_phone_info(
        country_code: int,
        number: int,
        numbers: IntervalCompressedInfo,
) -> tuple[Literal[True], str, str] | tuple[Literal[False], None, None]:
    if country_code != 7:
        raise UnknownCountryCode(f'Unknown code {country_code}. Currently, only Russian numbers are supported')

    info = numbers.get_info(number)
    if info is None:
        return False, None, None
    return True, info.operator, info.region
