from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 58d2a34bc2154443b17825bb4c653bc9
class Analyzer7 :
    def isValid(self, messages: List[Message]) -> bool:
        if not (len(messages) == 2):
            return False
        
        if not (messages[1]["sender"] == 'bot' and messages[1]["message"].startswith("Desculpe n\u00e3o entendi. Retornaremos")):
            return False
        
        return True

    def getQualifications(self, messages: List[Message]) -> Qualification:
        return {
            "selectedOption": 'Sem opção selecionada',
            "customerJourney": 'Sem opções selecionadas',
            "finalizationOfTheContract": 'Sem interação - Sem resposta do cliente',
        }
