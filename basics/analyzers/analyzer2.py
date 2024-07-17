from analyzer import ChatbotAnalyzer
from basics.find_ticket_by_id import Message
from typing import List, Dict

class Analyzer2(ChatbotAnalyzer) :
    def isValid(self, messages: List[Message]) -> bool:
        pass

    def getQualifications(self, messages: List[Message]) -> Dict[str, str]:
        pass
