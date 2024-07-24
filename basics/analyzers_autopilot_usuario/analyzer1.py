from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 6ba0009298df4b9893ce705291cba366

class Analyzer1 :

    def isValid(
        self,
        messagesclient: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesclient) == 12):
            return False
    
        if not (messagesclient[0]["sender"] == "client" and messagesclient[0]["message"].startswith("Ola")):
            return False
    
        if not (messagesclient[2]["sender"] == "client" and messagesclient[2]["message"].startswith("01472875532")):
            return False
    
        if not (messagesclient[4]["sender"] == "client" and messagesclient[4]["message"].startswith("3")):
            return False
    
        if not (messagesclient[6]["sender"] == "client" and messagesclient[6]["message"].startswith("0")):
            return False
    
        if not (messagesclient[8]["sender"] == "client" and messagesclient[8]["message"].startswith("10")):
            return False
    
        if not (messagesclient[10]["sender"] == "client" and messagesclient[10]["message"].startswith("Não")):
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
    