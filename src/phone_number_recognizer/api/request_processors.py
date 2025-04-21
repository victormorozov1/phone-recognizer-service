from functools import cached_property
from typing import TypedDict

from api.phones_data_loader import PhonesDataLoader
from api.serializers import PhoneCheckSerializer
from lib.phone_recognition.errors import UnknownCountryCode
from lib.phone_recognition.recognition import get_phone_info
from lib.request_processors import BaseRequestProcessor


class PhoneInfo(TypedDict, total=False):
    exists: bool
    operator: str
    region: str
    message: str


class RecognizePhoneRP(BaseRequestProcessor[dict]):
    def __init__(self, data_loader: PhonesDataLoader, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_loader = data_loader

    @cached_property
    def serializer(self) -> PhoneCheckSerializer:
        return PhoneCheckSerializer(data=self.data)

    def check(self) -> dict[str, list[str]]:
        self.serializer.is_valid()
        return self.serializer.errors

    def process(self) -> PhoneInfo:
        phone = self.serializer.validated_data['phone']
        country_code = int(phone[0])
        number = int(phone[1:])
        phones_data = self.data_loader.get_phones_data()
        try:
            found, operator, region = get_phone_info(country_code, number, phones_data)
        except UnknownCountryCode as e:
            return {'message': str(e)}
        if found:
            return {'exists': True, 'operator': operator, 'region': region}
        return {'exists': False}


class RecognizePhoneRPFabric:
    def __init__(self, filenames: list[str]):
        self.data_loader = PhonesDataLoader(filenames)

    def get_processor(self, data: dict) -> RecognizePhoneRP:
        return RecognizePhoneRP(self.data_loader, data)
