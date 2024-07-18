from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# a3436e09b33c4029838d7062445bf2bc

class Analyzer2 :

    def isValid(self, messages: List[Message]) -> bool:

        if not(len(messages) == 4):
            return False

        if not(messages[1]["sender"] == 'bot' and messages[1]["message"].startswith("Seja bem-vindo(a) à Nio Digital!")):
            return False

        if not (messages[3]["sender"] == "bot" and messages[3]["message"].startswith("Ótimo. Em que posso ajudar?")):
            return False
        
        return True

    def getQualifications(self, messages: List[Message]) -> Qualification:
        return {
            "selectedOption": 'Sem opção selecionada',
            "customerJourney":'Sem opções selecionadas',
            "finalizationOfTheContract": 'Sem interação - Sem resposta do cliente',
        }
