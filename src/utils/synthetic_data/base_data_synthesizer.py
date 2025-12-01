from abc import ABC, abstractmethod


class BaseDataSynthesizer(ABC):
    def __init__(self, ):
        pass

    @abstractmethod
    def synthesize(self):
        pass