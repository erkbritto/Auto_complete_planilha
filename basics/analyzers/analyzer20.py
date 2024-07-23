from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 7ee88521c13348198cd5c7db3e6bf799
class Analyzer20:

    def isValid(self, messages: List[Message]) -> bool:
        if not (len(messages) == 10):
            return False
        
        if not (messages[1]["sender"] == 'bot' and messages[1]["message"].startswith("Seja bem-vindo")):
            return False
        
        if not (messages[3]["sender"] == 'bot' and messages[3]["message"].startswith("\u00d3timo.")):
            return False
        
        if not (messages[5]["sender"] == 'bot' and messages[5]["message"].startswith("*Digite a op\u00e7\u00e3o desejada")):
            return False
        
        if not (messages[7]["sender"] == 'bot' and messages[7]["message"].startswith("*Digite a")):
            return False
        
        if not (messages[9]["sender"] == 'bot' and messages[9]["message"].startswith("Devido a um problema")):
            return False
        
        return True

    def getQualifications(self, messages: List[Message]) -> Qualification:
        return  {
            "selectedOption": 'Opção 1',
            "customerJourney": 'Selecionou 4 opções do menu',
            "finalizationOfTheContract": 'Sem interação - Sem resposta do cliente',
        }
