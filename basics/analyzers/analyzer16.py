from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 930eadceaa7340e7926561c80e6cdf5b
class Analyzer16:

    def isValid(self, messages: List[Message]) -> bool:
        if not(len(messages) == 8):
            return False
        if not (messages[1]["sender"] == 'bot' and messages[1]["message"].startswith("Seja")):
            return False
        if not (messages[3]["sender"] == 'bot' and  messages[3]["message"].startswith("\u00d3timo. Em que posso")):
            return False
        if not (messages[5]["sender"] == 'bot' and messages[5]["message"].startswith("O seu c\u00f3digo de rastreio")):
            return False
        if not (messages[7]["sender"] == 'bot' and messages[7]["message"].startswith("*Digite a op\u00e7\u00e3o desejada")):
            return False
        return True

    def getQualifications(self, messages: List[Message]) -> Qualification:
        return {
            "selectedOption": 'Opção 8',
            "customerJourney": 'Selecionou apenas 1 opção',
            "finalizationOfTheContract": 'Sem interação - Sem resposta do cliente',
        }
