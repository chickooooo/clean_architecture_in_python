from abc import ABC, abstractmethod


class Usecase(ABC):
    @abstractmethod
    def call(self, **kwargs):
        pass
