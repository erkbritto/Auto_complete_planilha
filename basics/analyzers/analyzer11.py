from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification
    #64eec7c661e84027808a364d6cd38267
class Analyzer11:
    def isValid(self, messages: List[Message]) -> bool:
        if not (len(messages) == 6):
            return False
        
        if not (messages[1]["sender"] == 'bot' and "Por favor, anote seu protocolo de atendimento" in messages[1]["message"]):
            return False
        
        if not (messages[3]["sender"] == 'bot' and "N\u00e3o conseguimos localizar o CPF informado, digite-o novamente, mas apenas os n\u00fameros, ok?" in messages[3]["message"]):
            return False
        
        if not (messages[5]["sender"] == 'bot' and "Que pena, mas n\u00e3o consegui localizar o CPF informado" in messages[5]["message"]):
            return False
        
        return True

    def getQualifications(self, messages: List[Message]) -> Qualification:
        return {
            "selectedOption": '',
            "customerJourney": '',
            "finalizationOfTheContract": '',
        }
