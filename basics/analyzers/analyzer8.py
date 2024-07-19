from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification
# d23c095bd54f4cf2bdcc16fa50c78edc
class Analyzer8 :
    def isValid(self, messages: List[Message]) -> bool:

        if not (len(messages) == 10):
            return False
        
        if not (messages[1]["sender"] == 'bot' and messages[1]["message"].startswith("Seja bem-vindo(a) \u00e0 Nio Digital!")):
            return False
        
        if not (messages[3]["sender"] == 'bot' and messages[3]["message"].startswith("\u00d3timo. Em que posso ajudar?")):
            return False
        
        if not (messages[5]["sender"] == 'bot' and messages[5]["message"].startswith("Por favor informe os 4 \u00faltimos d\u00edgitos")):
            return False
        
        if not (messages[7]["sender"] == 'bot' and messages[7]["message"].startswith("O \u00faltimos 4 d\u00edgitos que voc\u00ea digitou est\u00e1 inv\u00e1lido")):
            return False
        
        if not (messages[9]["sender"] == 'bot' and messages[9]["message"].startswith("Tudo bem!\nNio Digital agradece e at\u00e9 logo!")):
            return False

        return True

    def getQualifications(self, messages: List[Message]) -> Qualification:
        return {
            "selectedOption": 'Opção 1',
            "customerJourney": 'Selecionou 2 opções do menu',
            "finalizationOfTheContract": 'Contato finalizado por falta de dados corretos',
        }
