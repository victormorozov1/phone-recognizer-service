from abc import ABC, abstractmethod
from typing import Any


class BaseRequestProcessor[D: Any](ABC):
    def __init__(self, data: D):
        self.data = data

    @abstractmethod
    def check(self) -> list[Any]:
        pass

    @abstractmethod
    def process(self) -> Any:
        pass
