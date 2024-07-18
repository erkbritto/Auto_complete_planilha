from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 9a49940a58fb4fc7a18e033aa92c352e
class Analyzer4 :
    def isValid(self, messages: List[Message]) -> bool:
        
        if(len(messages) != 8):
            return False
        
        if not (messages[1]['sender'] == 'bot' and messages[1]['message'].startswith('Seja bem-vindo(a)') and "informe o n\u00famero do seu CPF" in messages[1]['message']):
            return False

        if not(messages[3]['sender'] == 'bot' and messages[3]['message'].startswith("\u00d3timo. Em que posso ajudar?")):
            return False
        
        if not(messages[5]['sender'] == 'bot' and messages[5]["message"].startswith("Por favor informe os 4 \u00faltimos d\u00edgitos do cart\u00e3o")):
            return False
        
        if not(messages[7]['sender'] == 'bot' and messages[7]['message'].startswith("Seguem as informa\u00e7\u00f5es solicitadas:")):
            return False

        return True
    def getQualifications(self, messages: List[Message]) -> Qualification:
        return {
            "selectedOption": 'Opção 1',
            "customerJourney": 'Selecionou apenas 1 opção',
            "finalizationOfTheContract": 'Sem interação - Sem resposta do cliente',
        }