from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 808a56533445406b95372be96e34c8b4

class Analyzer21 :

    def isValid(self, messages: List[Message]) -> bool:
        if not(len(messages) == 6 ): 
            return False

        if not(messages[1]["sender"] == 'bot' and messages[1]["message"].startswith("Desculpe n\u00e3o entendi.")):
            return False
        
        if not(messages[3]["sender"] == 'bot' and messages[1]["message"].startswith("N\u00e3o conseguimos localizar o CPF informado,")):
            return False
        
        if not(messages[5]["sender"] == 'bot' and messages[1]["message"].startswith("Que pena, mas n\u00e3o consegui localizar o CPF informado")):
            return False
        
        return True

    def getQualifications(self, messages: List[Message]) -> Qualification:
        return {
            "selectedOption": 'Sem opção selecionada',
            "customerJourney":'Sem opções selecionadas',
            "finalizationOfTheContract": 'Sem interação - Sem resposta do cliente',
        }
