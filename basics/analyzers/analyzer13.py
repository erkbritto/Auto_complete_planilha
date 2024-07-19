from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# ec76a312fd1248b18e3ec6b7149fba11

class Analyzer13:

    def isValid(self, messages: List[Message]) -> bool:
        if not (len(messages) == 8):
            return False
        
        if not (messages[1]["sender"] == 'bot' and messages[1]["message"].startswith("Desculpe não entendi")):
            return False
        
        if not (messages[3]["sender"] == 'bot' and messages[3]["message"].startswith("N\u00e3o conseguimos localizar")):
            return False
        
        if not (messages[5]["sender"] == 'bot' and messages[5]["message"].startswith("\u00d3timo. Em que posso ajudar?")):
            return False
        
        if not (messages[7]["sender"] == 'bot' and messages[7]["message"].startswith("Por favor informe os 4 \u00faltimos")):
            return False
        
        return True

    def getQualifications(self, messages: List[Message]) -> Qualification:
        return {
            "selectedOption": 'Opção 1',
            "customerJourney": 'Selecionou 2 opções do menu',
            "finalizationOfTheContract": 'Contato encerrado com script de finalização.',
        }
