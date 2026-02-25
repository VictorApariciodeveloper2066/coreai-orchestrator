# django_core/api/interfaces.py
from abc import ABC, abstractmethod

class AIProcessorInterface(ABC):
    @abstractmethod
    def process(self, text: str):
        pass