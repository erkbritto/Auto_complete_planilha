from abc import ABC, abstractmethod
from typing import List, Dict

class Mensagem:
    def __init__(self, sender: str, message: str):
        self.sender = sender
        self.message = message

class ChatbotAnalyzer(ABC):
    @abstractmethod
    def verifyStructure(self, messages: List[Mensagem]) -> bool:
        pass

    @abstractmethod
    def getQualifications(self, messages: List[Mensagem]) -> Dict[str, str]:
        pass
