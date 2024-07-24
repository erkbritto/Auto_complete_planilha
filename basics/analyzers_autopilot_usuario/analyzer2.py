from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 8f98f8dd08bf42fa8570cb2dc9c88ea6

class Analyzer2 :

    def isValid(
        self,
        messagesclient: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesclient) == 10):
            return False
    
        if not (messagesclient[0]["sender"] == "client" and messagesclient[0]["message"].startswith("Bom-dia  recebi o meu cartão , gostaria de saber qual é o limite dele")):
            return False
    
        if not (messagesclient[2]["sender"] == "client" and messagesclient[2]["message"].startswith("32182627120")):
            return False
    
        if not (messagesclient[4]["sender"] == "client" and messagesclient[4]["message"].startswith("1")):
            return False
    
        if not (messagesclient[6]["sender"] == "client" and messagesclient[6]["message"].startswith("4152")):
            return False
    
        if not (messagesclient[8]["sender"] == "client" and messagesclient[8]["message"].startswith("Sim")):
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
    