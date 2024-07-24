from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 245b50cd89314e2e8fc7c414c6764d22

class Analyzer1 :

    def isValid(
        self,
        messagesclient: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesclient) == 8):
            return False
    
        if not (messagesclient[0]["sender"] == "client" and messagesclient[0]["message"].startswith("Oi")):
            return False
    
        if not (messagesclient[2]["sender"] == "client" and messagesclient[2]["message"].startswith("08609517829")):
            return False
    
        if not (messagesclient[4]["sender"] == "client" and messagesclient[4]["message"].startswith("1")):
            return False
    
        if not (messagesclient[6]["sender"] == "client" and messagesclient[6]["message"].startswith("7053")):
            return False
    
        return True

    def getQualifications(
            self,
            messagesclient: List[Message],
            allMessages: List[Message],
        ) -> Qualification:
        return {
            "selectedOption": '',
            "customerJourney": '',
            "finalizationOfTheContract": 'nao qualificado',
        }
    