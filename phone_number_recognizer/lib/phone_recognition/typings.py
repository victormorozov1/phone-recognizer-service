from dataclasses import dataclass


@dataclass
class PhoneNumbersInterval:
    min_number: int
    max_number: int
    operator: str
    region: str
