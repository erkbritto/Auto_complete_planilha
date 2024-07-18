from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

class Analyzer19 :
    def isValid(self, messages: List[Message]) -> bool:
        return False

    def getQualifications(self, messages: List[Message]) -> Qualification:
        return {
            "selectedOption": '',
            "customerJourney": '',
            "finalizationOfTheContract": '',
        }