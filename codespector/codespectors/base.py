from abc import ABC, abstractmethod


class BaseCodeSpector(ABC):
    @abstractmethod
    def review(self, *args, **kwargs) -> None:
        raise NotImplementedError
