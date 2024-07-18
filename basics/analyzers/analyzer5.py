from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 371cc4ed5af147a8854ff0ac955f70e4
class Analyzer5 :
    
    def isValid(self, messages: List[Message]) -> bool:
        
        if not (len(messages) == 14):
            return False
        
        if not (messages[1]["sender"] == 'bot' and messages[1]["message"].startswith("Seja bem-vindo(a) \u00e0 Nio Digital!")):
            return False
        
        if not (messages[3]["sender"] == 'bot' and messages[3]["message"].startswith("\u00d3timo. Em que posso ajudar?")):
            return False
        
        if not (messages[5]["sender"] == 'bot' and messages[5]["message"].startswith("Por favor informe os 4 \u00faltimos d\u00edgitos")):
            return False
        
        if not (messages[7]["sender"] == 'bot' and "Tudo bem. Digite a op\u00e7\u00e3o desejada para" in messages[7]["message"]):
            return False
        
        if not (messages[9]["sender"] == 'bot' and messages[9]["message"].startswith("J\u00e1 faz mais de 5 dias que efetuou o pagamento da fatura?")):
            return False
        
        if not (messages[11]["sender"] == 'bot' and messages[11]["message"].startswith("Nesse caso, voc\u00ea dever\u00e1 aguardar")):
            return False
        
        if not (messages[13]["sender"] == 'bot' and messages[13]["message"].startswith("Tudo bem!\nNio Digital agradece e at\u00e9 logo!")):
            return False
        
        return True

    def getQualifications(self, messages: List[Message]) -> Qualification:
        return {
            "selectedOption": 'Opção 2',
            "customerJourney": 'Selecionou 2 opções do menu',
            "finalizationOfTheContract": 'Contato encerrado com script de finalização.',
        }
