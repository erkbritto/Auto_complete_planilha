from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 0bf1667e2de342e8b527b83f5c58618c

class Analyzer10:

    def isValid(self, messages: List[Message]) -> bool:

        if not(len(messages) == 6):
            return False

        if not(messages[1]["sender"] == 'bot' and messages[1]["message"].startswith("Seja bem-vindo(a) \u00e0 Nio Digital!")):
            return False

        if not (messages[3]["sender"] == "bot" and messages[3]["message"].startswith("\u00d3timo. Em que posso ajudar?\n\u3164 *Digite a op\u00e7\u00e3o desejada para*:")):
            return False
        
        if not (messages[5]["sender"] == 'bot' and messages[5]["message"].startswith("Por favor informe os 4 \u00faltimos d\u00edgitos do cart\u00e3o que deseja consultar.")):
            return False
        
        return True

    def getQualifications(self, messages: List[Message]) -> Qualification:
        return {
            "selectedOption": 'Opção 1',
            "customerJourney": 'Selecionou apenas 1 opção',
            "finalizationOfTheContract": 'Sem interação - Sem resposta do cliente',
        }
