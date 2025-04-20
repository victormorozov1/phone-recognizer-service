from lib.phone_recognition.errors import UnknownCountryCode
from lib.phone_recognition.intervals_compressed_info import IntervalCompressedInfo


def get_phone_info(
        country_code: int,
        number: int,
        numbers: IntervalCompressedInfo,
) -> tuple[bool, str | None, str | None]:

    if country_code != 7:
        raise UnknownCountryCode('Currently, only Russian numbers are supported')

    info = numbers.get_info(number)
    if info is None:
        return False, None, None
    return True, info.operator, info.region
