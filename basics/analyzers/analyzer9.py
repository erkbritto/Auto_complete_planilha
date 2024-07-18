from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification
    #592d0a9c01694c1dbe45df06fba1c863
class Analyzer9:
    def isValid(self, messages: List[Message]) -> bool:

        if not (len(messages) == 10):
            return False
        
        if not (messages[1]["sender"] == 'bot' and messages[0]["message"].startswith("Seja bem-vindo(a) \u00e0 Nio Digital!")):
            return False
        
        if not (messages[2]["sender"] == 'bot' and messages[0]["message"].startswith("N\u00e3o conseguimos localizar o CPF informado")):
            return False
        
        if not (messages[0]["sender"] == 'bot' and messages[0]["message"].startswith("\u00d3timo. Em que posso ajudar?")):
            return False
        
        if not (messages[7]["sender"] == 'bot' and messages[0]["message"].startswith("Por favor informe os 4 \u00faltimos d\u00edgitos do cart\u00e3o que deseja consultar.")):
            return False
        
        if not (messages[9]["sender"] == 'bot' and messages[0]["message"].startswith("Tudo bem. Digite a op\u00e7\u00e3o desejada para:")):
            return False
        
        if not (messages[0]["sender"] == 'bot' and messages[0]["message"].startswith("Digite a op\u00e7\u00e3o desejada para:")):
            return False
        if not (messages[9]["sender"] == 'bot' and messages[0]["message"].startswith("Digite:\n\n1 - Dificuldade em efetuar compras com o cart\u00e3o.\n2 - Outros assuntos.\n3 - Retornar ao menu anterior.")):
            return False
        if not (messages[2]["sender"] == 'bot' and messages[0]["message"].startswith("S\u00f3 um momento enquanto te transferimos para um de nossos agentes.")):
            return False
        
        return True

    def getQualifications(self, messages: List[Message]) -> Qualification:
        return {
            "selectedOption": '',
            "customerJourney": '',
            "finalizationOfTheContract": '',
        }
