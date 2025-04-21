import pytest

from lib.phone_recognition.load import load_from_files
from lib.phone_recognition.recognition import get_phone_info

NUMBERS_DATA = load_from_files(
    [
        'tests/data/data1.csv',
        'tests/data/data2.csv',
    ],
)


@pytest.mark.parametrize(
    ('country_code', 'number', 'expected_found', 'expected_operator', 'expected_region'),
    (
            (7, 2229485566, True, 'ООО "sim sim"', 'г. Москва и Московская область'),
            (7, 6012200000, True, 'АО "BEBRA"', 'г. Калининград'),
            (7, 6012200999, True, 'АО "BEBRA"', 'г. Калининград'),
            (7, 6012201000, False, None, None),
    )
)
def test_phone_recognition(
        country_code: int,
        number: int,
        expected_found: bool,
        expected_operator: str,
        expected_region: str,
):
    found, operator, region = get_phone_info(country_code, number, NUMBERS_DATA)
    assert found == expected_found
    assert operator == expected_operator
    assert region == expected_region
