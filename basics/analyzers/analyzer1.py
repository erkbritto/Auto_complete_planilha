from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

class Analyzer1 :
    def isValid(self, messages: List[Message]) -> bool:

        return len(messages) == 6

    def getQualifications(self, messages: List[Message]) -> Qualification:
        pass
