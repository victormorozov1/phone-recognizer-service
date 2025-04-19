from functools import cached_property
from typing import TypedDict

from api.serializers import PhoneCheckSerializer
from lib.request_processors import BaseRequestProcessor


class RecognizePhoneStatusDict(TypedDict):
    valid: bool


class RecognizePhoneRequestProcessor(BaseRequestProcessor[dict]):
    @cached_property
    def serializer(self) -> PhoneCheckSerializer:
        return PhoneCheckSerializer(data=self.data)

    def check(self) -> dict[str, list[str]]:
        self.serializer.is_valid()
        return self.serializer.errors

    def process(self) -> RecognizePhoneStatusDict:
        return {'valid': True}
