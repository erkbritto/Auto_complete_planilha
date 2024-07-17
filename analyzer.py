from abc import AbstractClass, abstractmethod
from typing import List, Dict
from basics.find_ticket_by_id import Message

class ChatbotAnalyzer(AbstractClass):
    @abstractmethod
    def isValid(self, messages: List[Message]) -> bool:
        pass

    @abstractmethod
    def getQualifications(self, messages: List[Message]) -> Dict[str, str]:
        pass
