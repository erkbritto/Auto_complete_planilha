from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 079b6840caa14ae8bdb785cfed202fa4
class Analyzer13:
    def isValid(self, messages: List[Message]) -> bool:
        if not (len(messages) == 15):
            return False
        
        if not (messages[1]["sender"] == 'bot' and "Por favor, anote seu protocolo de atendimento" in messages[1]["message"]):
            return False
        
        if not (messages[3]["sender"] == 'bot' and "Em que posso ajudar?" in messages[3]["message"]):
            return False
        
        if not (messages[5]["sender"] == 'bot' and "Por favor informe os 4 \u00faltimos d\u00edgitos do cart\u00e3o que deseja consultar." in messages[5]["message"]):
            return False
        
        if not (messages[7]["sender"] == 'bot' and "*Tudo bem. Digite a op\u00e7\u00e3o desejada para*:" in messages[7]["message"]):
            return False
        
        if not (messages[9]["sender"] == 'bot' and "J\u00e1 faz mais de 5 dias que efetuou o pagamento da fatura?" in messages[9]["message"]):
            return False
        
        if not (messages[11]["sender"] == 'bot' and "Olha, no momento n\u00e3o consta pagamento em nosso sistema." in messages[11]["message"]):
            return False
        
        if not (messages[13]["sender"] == 'bot' and "Devido a um problema t\u00e9cnico na gera\u00e7\u00e3o das faturas" in messages[13]["message"]):
            return False
        
        if not (messages[14]["sender"] == 'bot' and "Tudo bem! Nio Digital agradece e at\u00e9 logo!" in messages[14]["message"]):
            return False
        
        return True

    def getQualifications(self, messages: List[Message]) -> Qualification:
        return {
            "selectedOption": 'Opção 2',
            "customerJourney": 'Selecionou 3 opções do menu',
            "finalizationOfTheContract": 'Contato encerrado com script de finalização.',
        }