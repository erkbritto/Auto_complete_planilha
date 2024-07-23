from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# d935804cff1640dcb6a1393dffaa4fce
class Analyzer17:

    def isValid(self, messages: List[Message]) -> bool:
        if not (len(messages) == 10):
            return False
        
        if not (messages[1]["sender"] == 'bot' and messages[1]["message"].startswith("Seja bem-vindo")):
            return False
        
        if not (messages[3]["sender"] == 'bot' and messages[3]["message"].startswith("\u00d3timo.")):
            return False
        
        if not (messages[5]["sender"] == 'bot' and messages[5]["message"].startswith("Por favor informe")):
            return False
        
        if not (messages[7]["sender"] == 'bot' and messages[7]["message"].startswith("Seguem as informa\u00e7\u00f5es")):
            return False

        if not (messages[9]["sender"] == 'bot' and messages[9]["message"].startswith("Ol\u00e1 Seja bem-vindo")):
            return False

        return True

    def getQualifications(self, messages: List[Message]) -> Qualification:
        return {
            "selectedOption": 'Opção 1',  
            "customerJourney": 'Selecionou apenas 1 opção',
            "finalizationOfTheContract": 'Sem interação - Sem resposta do cliente',
        }
